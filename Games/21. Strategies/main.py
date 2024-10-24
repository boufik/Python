from random import shuffle
import matplotlib.pyplot as plt

# Function 1
def createCards():

    cards = []
    for i in range(1, 14):
        for times in range(4):
            cards.append(i)
    shuffle(cards)
    shuffle(cards)
    return cards


# Function 2
def convert(cards):

    cards2 = cards
    for i in range(len(cards)):
        if cards[i] == 11 or cards[i] == 12 or cards[i] == 13:
            cards2[i] = 10
    return cards2


# Function 3
def aces(xartia):

    counter = 0
    no_aces = []
    for i in range(len(xartia)):
        if xartia[i] == 1:
            counter += 1
        else:
            no_aces.append(xartia[i])
    return counter, no_aces

# Function 4
def rules(xartia):

    SUM = 0        # IN CASE OF 1 ACE, AFTER I WILL ADD +10 IN CASE OF 11
    SUM2 = -1000   # IT WILL BE +10 IF I HAVE 1 ACE, OTHERWISE SUM1 = SUM2
    counter, no_aces = aces(xartia)
    if counter == 0:
        SUM = sum(xartia)
        SUM2 = SUM
    elif counter == 4:
        SUM = 24
        SUM = SUM + sum(no_aces)
        SUM2 = SUM
    elif counter == 3:
        SUM = 1 + 11 + 1
        SUM = SUM + sum(no_aces)
        SUM2 = SUM
    elif counter == 2:
        SUM = 1 + 11
        SUM = SUM + sum(no_aces)
        SUM2 = SUM
    elif counter == 1:                      # TO METRAEI MONO GIA +1 OXI SYN 11 PROS TO PARON
        SUM = 1
        SUM = SUM + sum(no_aces)
        SUM2 = SUM + 10
    else:
        print("Error in function '" + rules.__name__ + "'")

    return SUM, SUM2


# Function 5
def define_sum(xartia):

    SUM = -1000
    SUM1, SUM2 = rules(xartia)
    if SUM1 == SUM2:
        SUM = SUM1
    else:
        # We are in the case of 1 ace, 2 different sums (SUM2 = SUM1 + 10)
        if SUM2 <= 21:
            SUM = SUM2
        else:
            # SUM2 = 23 for example, I have to take the SUM1
            SUM = SUM1
    return SUM



# FUNCTION 6
def AI_user(user_cards, cards, target_user, offset_user):

    user_sum = define_sum(user_cards)
    if user_sum < target_user:
        # Prepei na proxwrisw
        user_cards.append(cards[offset_user])
        offset_user += 1
        return AI_user(user_cards, cards, target_user, offset_user)
    else:
        return user_cards, cards, target_user, offset_user


# FUNCTION 7
def AI_mana(mana_cards, cards, stop_mana_tie, offset_mana, user_sum):

    # H mana proxwraei se 2 cases:
    # 1. An exei sum katw apo tou user_sum
    # 2. Se isopalia mporei na proxwrhsei mono an einai <= stop_mana_tie
    mana_sum = define_sum(mana_cards)
    if mana_sum < user_sum or mana_sum <= stop_mana_tie - 1:
        # Prepei na proxwrisw
        mana_cards.append(cards[offset_mana])
        offset_mana += 1
        return AI_mana(mana_cards, cards, stop_mana_tie, offset_mana, user_sum)
    else:
        return mana_cards, cards, stop_mana_tie, offset_mana, user_sum



# FUNCTION 8
def simulate_round(target_user, stop_mana_tie):

    # 1. Create cards
    cards = createCards()
    cards = convert(cards)

    # 2. The first two cards are fixed, so cards are the last 50 cards
    # print("Cards = " + str(cards))
    user_first = cards[0]
    mana_first = cards[1]
    cards = cards[2:]                   # Cards now have a length of 50

    # 3. Data for AI calculations
    user_cards = [user_first]
    mana_cards = [mana_first]
    offset_user = 0                 # Poses kartes exei parei


    # 3. AI user
    user_cards, cards, target_user, offset_user = AI_user(user_cards, cards, target_user, offset_user)
    user_sum = define_sum(user_cards)
    # print("User: sum = " + str(user_sum) + ", cards = " + str(user_cards))

    # 4. AI mana
    offset_mana = offset_user
    mana_cards, cards, stop_mana_tie, offset_mana, user_sum = AI_mana(mana_cards, cards, stop_mana_tie, offset_mana, user_sum)
    mana_sum = define_sum(mana_cards)
    # print("Mana: sum = " + str(mana_sum) + ", cards = " + str(mana_cards))
    return user_sum, mana_sum


# FUNCTION 9
def simulate_round_winner(target_user, stop_mana_tie):

    user_sum, mana_sum = simulate_round(target_user, stop_mana_tie)
    winner = -1000                   # winner = 1 for user win, winner = 0 for a tie result and winner = -1 for mana win
    if user_sum > 21:
        winner = -1
        # print("Mana wins!")
    else:
        if mana_sum > 21:
            winner = 1
            # print("User wins!")
        else:                                       # In case of 2 sums <= 21
            if user_sum > mana_sum:
                winner = 1
                # print("User wins!")
            elif user_sum < mana_sum:
                winner = -1
                # print("Mana wins!")
            else:
                winner = 0
                # print("It's a tie!")
    # print()
    return winner




# FUNCTION 10
def simulate_stats(target_user, stop_mana_tie, num_of_sims):

    print("******************************************************************")
    print(" Target user:     " + str(target_user))
    print("Stop mana tie:    " + str(stop_mana_tie))
    user_wins = 0
    mana_wins = 0
    ties = 0
    for i in range(num_of_sims):
        # print("******** ROUND " + str(i + 1) + " ********")
        winner = simulate_round_winner(target_user, stop_mana_tie)
        if winner == 1:
            user_wins += 1
        elif winner == -1:
            mana_wins += 1
        else:
            ties += 1
    # print()
    # print()
    print(" Simulations:     " + str(num_of_sims))
    print("   User wins:     " + str(user_wins) + " (" + str(100 * user_wins / num_of_sims) + "%)")
    print("   Mana wins:     " + str(mana_wins) + " (" + str(100 * mana_wins / num_of_sims) + "%)")
    print("       Ties:      " + str(ties) + " (" + str(100 * ties / num_of_sims) + "%)")
    print()
    return user_wins, mana_wins, ties



# MAIN FUNCTION
# Data lists
target_user_list = [15, 16, 17]                    # AN FTASW SE AYTO, STOP
stop_mana_tie_list = [16, 17, 18]                  # AN H MANA EINAI ISOPALIA ME TON USER SE AYT, STOP, PIO KATW PROXWRAEI
num_of_sims = 1000
x_list = []
y_list = []
user_wins_perc_list = []
mana_wins_perc_list = []
ties_perc_list = []

for target_user in target_user_list:
    for stop_mana_tie in stop_mana_tie_list:
        x_list.append(target_user)
        y_list.append(stop_mana_tie)
        user_wins, mana_wins, ties = simulate_stats(target_user, stop_mana_tie, num_of_sims)
        user_wins_perc_list.append(100 * user_wins / num_of_sims)
        mana_wins_perc_list.append(100 * mana_wins / num_of_sims)
        ties_perc_list.append(100 * ties / num_of_sims)

print("******************************************************************")
print("Mana wins percentage list:" + str(mana_wins_perc_list))
print("User wins percentage list:" + str(user_wins_perc_list))
print("   Ties percentage list:  " + str(ties_perc_list))
print()
print("Average mana win percentage = " + str(sum(mana_wins_perc_list) / len(mana_wins_perc_list)) + " %")
print("Average user win percentage = " + str(sum(user_wins_perc_list) / len(user_wins_perc_list)) + " %")
print("   Average tie percentage =   " + str(sum(ties_perc_list) / len(ties_perc_list)) + " %")



# Plots
# I will make plots = # stop_mana_ties for every value of them
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x_list, y_list, mana_wins_perc_list, 'blue')
ax.scatter(x_list, y_list, user_wins_perc_list, 'red')
ax.scatter(x_list, y_list, ties_perc_list, 'green')
ax.set_xlabel('Target user')
ax.set_ylabel('Stop mana tie')
ax.set_zlabel('Percentages')
plt.legend(["Mana wins perc", "User wins perc", "Ties perc"])
plt.show()