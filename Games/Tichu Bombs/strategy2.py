"""
Balanced Tichu exchange heuristic with a distinct retention trade-off.
Default: 250,000 complete four-player deals = 1,000,000 player-hands.
Requires: numpy
"""

import argparse
import numpy as np

N_PLAYERS, HAND_SIZE, DECK_SIZE = 4, 14, 56

# Higher scores mean "keep this card". The three lowest-scoring cards are passed.
STRATEGY = {
    "name": "Balanced",
    "rank_weight": 0.45,
    "pair_bonus": 6.0,
    "triple_bonus": 14.0,
    # When a triple also supports a normal straight, prefer one copy for the run over all three.
    "triple_in_run_bonus": 10.0,
    "normal_run_rewards": {3: 3.0, 4: 6.0, 5: 9.0},
    "adjacent_bonus": 2.0,
    "distance_two_bonus": 0.8,
    "four_run_bonus": 7.0,
    "special_scores": {52: 5.0, 53: 1.5, 54: 8.0, 55: 9.0},
}


def deal_batch(rng: np.random.Generator, batch_size: int) -> np.ndarray:
    # A random permutation deals every card exactly once and produces four 14-card hands.
    return rng.random((batch_size, DECK_SIZE)).argsort(axis=1).reshape(
        batch_size, N_PLAYERS, HAND_SIZE
    ).astype(np.int16)


def card_presence(hands: np.ndarray) -> np.ndarray:
    # presence[b,p,s,r] is true only when player p has rank r in suit s.
    presence = np.zeros((hands.shape[0], N_PLAYERS, 4, 13), dtype=bool)
    for suit in range(4):
        for rank in range(13):
            presence[:, :, suit, rank] = np.any(hands == rank * 4 + suit, axis=2)
    return presence


def bomb_hands(hands: np.ndarray, presence: np.ndarray) -> np.ndarray:
    # Four cards of one rank form a bomb; special cards are not part of four-of-a-kind.
    rank_counts = presence.sum(axis=2)
    four_of_a_kind = np.any(rank_counts == 4, axis=2)

    # A straight-flush bomb is any five consecutive ranks in one suit (no Ace-low wrap).
    straight_flush = np.zeros(hands.shape[:2], dtype=bool)
    for suit in range(4):
        for start_rank in range(9):
            straight_flush |= np.all(
                presence[:, :, suit, start_rank : start_rank + 5], axis=2
            )
    return four_of_a_kind | straight_flush


def protect_existing_bombs(hands: np.ndarray, presence: np.ndarray) -> np.ndarray:
    """Lock existing bomb cards, while leaving at least three cards available to pass.

    If an exceptionally bomb-rich hand has more than 11 bomb cards, preserve as many
    complete bombs as fit. Four-of-a-kinds are considered before straight flushes.
    """
    locked = np.zeros_like(hands, dtype=bool)
    rank_counts = presence.sum(axis=2)

    # Lock complete four-of-a-kind sets first; each candidate is exactly four cards.
    for rank in range(13):
        is_quad = rank_counts[:, :, rank] == 4
        candidate = (hands // 4 == rank) & (hands < 52) & is_quad[:, :, None]
        can_add = locked.sum(axis=2) + 4 <= 11
        locked |= candidate & can_add[:, :, None]

    # Then lock straight-flush windows when their union still leaves three passable cards.
    for suit in range(4):
        for start_rank in range(9):
            run_exists = np.all(
                presence[:, :, suit, start_rank : start_rank + 5], axis=2
            )
            candidate = np.zeros_like(locked)
            for rank in range(start_rank, start_rank + 5):
                candidate |= (hands == rank * 4 + suit) & run_exists[:, :, None]
            newly_locked = (candidate & ~locked).sum(axis=2)
            can_add = run_exists & (locked.sum(axis=2) + newly_locked <= 11)
            locked |= candidate & can_add[:, :, None]

    return locked


def retention_scores(hands: np.ndarray, presence: np.ndarray) -> np.ndarray:
    """Score cards by conservative hand-building value; larger scores are retained."""
    suited = hands < 52
    ranks = hands // 4
    scores = np.where(suited, (ranks + 1) * STRATEGY["rank_weight"], 0.0).astype(np.float32)

    # Detect rank runs across all suits: these are ordinary straight opportunities, not bombs.
    # Strategy 2 values these runs; strategies 1 and 3 intentionally do not prioritize them.
    rank_presence = presence.any(axis=2)
    normal_run_support = np.zeros(rank_presence.shape, dtype=np.float32)
    for run_length, reward in STRATEGY["normal_run_rewards"].items():
        for start_rank in range(14 - run_length):
            run = np.all(
                rank_presence[:, :, start_rank : start_rank + run_length], axis=2
            )
            for rank in range(start_rank, start_rank + run_length):
                normal_run_support[:, :, rank] = np.maximum(
                    normal_run_support[:, :, rank], run * reward
                )

    # Preserve pairs and triples for four-of-a-kind potential, but strategy 2 may
    # break a triple when its rank is already part of a promising normal straight.
    rank_counts = presence.sum(axis=2)
    for rank in range(13):
        group = suited & (ranks == rank)
        count = rank_counts[:, :, rank, None]
        run_support = normal_run_support[:, :, rank, None]
        triple_bonus = np.where(
            run_support > 0,
            STRATEGY["triple_in_run_bonus"],
            STRATEGY["triple_bonus"],
        )
        bonus = np.where(count == 2, STRATEGY["pair_bonus"],
                 np.where(count == 3, triple_bonus, 0.0))
        scores += group * bonus

        # Only one copy of a duplicated rank is needed for a straight; reward that copy.
        if STRATEGY["normal_run_rewards"]:
            min_card = np.min(np.where(group, hands, 999), axis=2)[:, :, None]
            representative = group & (hands == min_card)
            scores += representative * run_support

    # Reward same-suit neighbours and near-neighbours, which help build long sequences.
    adjacency = np.zeros_like(presence, dtype=np.float32)
    adjacency[:, :, :, 1:] += presence[:, :, :, :-1] * STRATEGY["adjacent_bonus"]
    adjacency[:, :, :, :-1] += presence[:, :, :, 1:] * STRATEGY["adjacent_bonus"]
    adjacency[:, :, :, 2:] += presence[:, :, :, :-2] * STRATEGY["distance_two_bonus"]
    adjacency[:, :, :, :-2] += presence[:, :, :, 2:] * STRATEGY["distance_two_bonus"]

    # A 4-card suited run is one card away from a straight-flush bomb, so reward it extra.
    in_four_run = np.zeros_like(presence)
    for suit in range(4):
        for start_rank in range(10):
            run = np.all(presence[:, :, suit, start_rank : start_rank + 4], axis=2)
            for rank in range(start_rank, start_rank + 4):
                in_four_run[:, :, suit, rank] |= run

    # Gather each card's sequence support from its suit/rank position in the hand.
    batch_idx = np.arange(hands.shape[0])[:, None, None]
    player_idx = np.arange(N_PLAYERS)[None, :, None]
    suits = hands % 4
    safe_ranks = np.minimum(ranks, 12)  # Special cards are masked out below.
    scores += adjacency[batch_idx, player_idx, suits, safe_ranks] * suited
    scores += in_four_run[batch_idx, player_idx, suits, safe_ranks] * suited * STRATEGY["four_run_bonus"]

    # Special-card values reflect their general trick utility; Dog is easiest to pass here.
    for card_id, value in STRATEGY["special_scores"].items():
        scores += (hands == card_id) * value

    return scores


def exchange(hands: np.ndarray, scores: np.ndarray) -> np.ndarray:
    """Pass the three lowest-scoring cards: one left, one to partner, one right."""
    order = np.argsort(scores, axis=2)
    outgoing = np.take_along_axis(hands, order[:, :, :3], axis=2)
    kept = np.take_along_axis(hands, order[:, :, 3:], axis=2)

    # The lowest-value pass goes to one opponent, the next-lowest to the other,
    # and the best of the three pass cards is reserved for the partner.
    outgoing_for_recipients = outgoing.copy()
    outgoing_for_recipients[:, :, 1] = outgoing[:, :, 2]
    outgoing_for_recipients[:, :, 2] = outgoing[:, :, 1]
    incoming = np.empty((hands.shape[0], N_PLAYERS, 3), dtype=np.int16)

    # Slot 0 is sent left, slot 1 to the opposite partner, and slot 2 to the right.
    for player in range(N_PLAYERS):
        incoming[:, player, 0] = outgoing_for_recipients[:, (player + 1) % 4, 0]
        incoming[:, player, 1] = outgoing_for_recipients[:, (player + 2) % 4, 1]
        incoming[:, player, 2] = outgoing_for_recipients[:, (player - 1) % 4, 2]

    return np.concatenate((kept, incoming), axis=2)


def run_simulation(games: int, seed: int, chunk_size: int) -> tuple[int, int]:
    rng = np.random.default_rng(seed)
    bomb_count = 0
    player_hand_count = 0

    for offset in range(0, games, chunk_size):
        batch_size = min(chunk_size, games - offset)
        hands = deal_batch(rng, batch_size)
        presence = card_presence(hands)

        # Existing bombs are protected before the three outgoing cards are selected.
        scores = retention_scores(hands, presence)
        locked = protect_existing_bombs(hands, presence)
        scores = np.where(locked, 1_000_000.0, scores)

        final_hands = exchange(hands, scores)
        final_presence = card_presence(final_hands)
        bomb_count += int(bomb_hands(final_hands, final_presence).sum())
        player_hand_count += batch_size * N_PLAYERS

    return bomb_count, player_hand_count


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--games", type=int, default=250_000)
    parser.add_argument("--seed", type=int, default=20261115)
    parser.add_argument("--chunk-size", type=int, default=5_000)
    args = parser.parse_args()
    if args.games <= 0 or args.chunk_size <= 0:
        parser.error("--games and --chunk-size must be positive")

    bombs, total_hands = run_simulation(args.games, args.seed, args.chunk_size)
    probability = 100.0 * bombs / total_hands
    print(f"Post-exchange bomb probability ({STRATEGY['name']}): {probability:.4f}% "
          f"({bombs:,}/{total_hands:,} player-hands)")


if __name__ == "__main__":
    main()
