"""
Estimate the pre-exchange probability of a Tichu bomb in a player's hand.
Default: 250,000 complete four-player deals = 1,000,000 player-hands.
Requires: numpy
"""

import argparse
import numpy as np

N_PLAYERS = 4
HAND_SIZE = 14
DECK_SIZE = 56


def deal_batch(rng: np.random.Generator, batch_size: int) -> np.ndarray:
    """
    Shuffle all 56 distinct cards and deal 14 to each of the four players.
    """
    # Sorting independent random keys gives each deck permutation equal probability.
    return rng.random((batch_size, DECK_SIZE)).argsort(axis=1).reshape(
        batch_size, N_PLAYERS, HAND_SIZE
    ).astype(np.int16)


def card_presence(hands: np.ndarray) -> np.ndarray:
    """
    Return presence[deal, player, suit, rank] for the 52 suited cards.
    """
    batch_size = hands.shape[0]
    presence = np.zeros((batch_size, N_PLAYERS, 4, 13), dtype=bool)
    # The four special cards (IDs 52-55) are deliberately excluded from rank/suit sets.
    for suit in range(4):
        for rank in range(13):
            card_id = rank * 4 + suit
            presence[:, :, suit, rank] = np.any(hands == card_id, axis=2)
    return presence


def bomb_hands(hands: np.ndarray, presence: np.ndarray) -> np.ndarray:
    """
    Return one Boolean per player: four-of-a-kind OR a 5+ straight flush.
    """
    # Four-of-a-kind: all four suits of at least one ordinary rank are in the hand.
    rank_counts = presence.sum(axis=2)
    four_of_a_kind = np.any(rank_counts == 4, axis=2)

    # Straight flush: any five consecutive ranks in one suit; Ace does not wrap to 2.
    straight_flush = np.zeros(hands.shape[:2], dtype=bool)
    for suit in range(4):
        for start_rank in range(9):  # 2..10 are the nine possible 5-card starts.
            straight_flush |= np.all(
                presence[:, :, suit, start_rank : start_rank + 5], axis=2
            )

    return four_of_a_kind | straight_flush


def run_simulation(games: int, seed: int, chunk_size: int) -> tuple[int, int]:
    rng = np.random.default_rng(seed)
    bomb_count = 0
    player_hand_count = 0

    for offset in range(0, games, chunk_size):
        batch_size = min(chunk_size, games - offset)
        hands = deal_batch(rng, batch_size)
        presence = card_presence(hands)
        bomb_count += int(bomb_hands(hands, presence).sum())
        player_hand_count += batch_size * N_PLAYERS

    return bomb_count, player_hand_count


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--games", type=int, default=250_000,
                        help="number of four-player deals (default: 250000)")
    parser.add_argument("--seed", type=int, default=20261115)
    parser.add_argument("--chunk-size", type=int, default=5_000)
    args = parser.parse_args()

    if args.games <= 0 or args.chunk_size <= 0:
        parser.error("--games and --chunk-size must be positive")

    bombs, total_hands = run_simulation(args.games, args.seed, args.chunk_size)
    probability = 100.0 * bombs / total_hands
    print(f"Pre-exchange bomb probability: {probability:.4f}% "
          f"({bombs:,}/{total_hands:,} player-hands)")


if __name__ == "__main__":
    main()
