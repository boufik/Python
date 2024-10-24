from random import randrange
from matplotlib import pyplot as plt


# Function 1 - Simulate the 2x-bet
def betx2(money, target, DIAIRETIS):
    if money >= target:
        print("Error while uging the function '" + betx2.__name__ +"'")
        return -1000
    initialMoney = money
    tries = 0
    wins = 0
    losses = 0
    lossStreak = 0
    bets = list()
    stats01 = list()
    firstBet = int(money / DIAIRETIS)

    # I will simulate the simulation with another way: red will be if my number is between 1 and 18,
    # black will be if my number is between 19 and 36 and "0" will be number 37


    while money > 0 and money < target:
        tries += 1
        # HERE I MUST CHECK IF I CAN DOUBLE MY MONEY
        # There is a possibility to happen this: money = 10, but next bet must be sth like 80 in order to win
        # So, bet will be all the remaining money
        print("************************ Try ", tries, "************************")
        canIDouble = (money > (firstBet)* (2**lossStreak))

        if canIDouble == True:
            # The bet will be determined by the lossStreak
            bet = firstBet * (2**lossStreak)
            bets.append(bet)
        else:
            bet = money
            bets.append(bet)
        money = money - bet
        # We will suppose that our user ALWAYS bets 'red', so we want the random generated number to be
        # between 1 and 18
        randomNumber = randrange(0, 37)
        print("Bet =", bet, ", randomNumber =", randomNumber)
        if randomNumber >= 1 and randomNumber <= 18:
            wins += 1
            lossStreak = 0
            money += 2 * bet
            stats01.append(1)
            print("You won, because 1 <=", randomNumber, "<= 18")
            print("Current money: ", money)
        elif randomNumber >= 19 and randomNumber <= 36:
            losses += 1
            lossStreak += 1
            stats01.append(0)
            print("You lost, because 19 <=", randomNumber, "<= 36")
            print("Current money: ", money)
        else:
            stats01.append(0)
            losses += 1
            lossStreak += 1
            print("You lost, because randomNumber = 0 ----> green color")
            print("Current money: ", money)
        print("*******************************************************")
        print()


    # Now, the basic process has finished. The remaining stuff is to show the stats in the user and the plot of his luck
    print()
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("Here, I will present you the stats of your gameplay.")
    print("Tries =", tries, ", wins =", wins, ", losses =", tries - wins)
    winPercentage = wins / tries
    winPercentage = round(10000 * winPercentage) / 10000
    print("Win percentage  = ", str(wins), "/", str(tries), "=", 100 * winPercentage, "%")
    print()
    gain = money - initialMoney
    gainPercentage = gain / initialMoney
    gainPercentage = round(10000 * gainPercentage) / 10000
    print("Initial money =", initialMoney, ", Final Money =", money, "(", 100 * gainPercentage, "%)")
    # Plotting our data
    plt.plot(stats01, 'ro')
    plt.title("0 = Loss, 1 = Win")
    plt.xlabel("Rounds")
    plt.ylabel("Win/Loss")
    plt.show()
    plt.plot(bets, 'bx')
    plt.title("Bets value per round")
    plt.xlabel("Rounds")
    plt.ylabel("Bet")
    plt.show()


# **********************************************************************************************************
# ********************************** MAIN FUNCTION *********************************************************
# **********************************************************************************************************
print("Welcome to the Roulette game. Rules are simple. You can only bet in red color")
money = int(input("Money here: "))
while money < 0:
    money = int(input("Money here: "))
target = int(input("Target money here: "))
while target <= money:
    target = int(input("Target money here: "))
DIAIRETIS = 50
betx2(money, target, DIAIRETIS)