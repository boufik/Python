from random import randrange

# Function 1
def makeGuess(random1):
    return "upper" if random1 <= 50 else "lower"

# Function 2
def correctGuess(random1, random2):
    return "upper" if random2 > random1 else "lower"

# Function 3
def determineWin(guess, correct):
    return True if guess == correct else False

# Function 4
def simulate():
    LIMIT = 10
    wins = 0
    result = ""
    # Initialization
    rounds = 1
    result += ("Round " + str(rounds)) + "\n"
    random1 = randrange(1, 101)
    guess = makeGuess(random1)
    random2 = randrange(1, 101)
    while random2 == random1:
        random2 = randrange(1, 101)
    correct = correctGuess(random1, random2)
    didIWin = determineWin(guess, correct)
    if didIWin == True:
        wins += 1
    result += ("r1 = " + str(random1) + " ----> guess = " + str(guess)) + "\n"
    result += ("r2 = " + str(random2) + " ----> Guess was " + str(didIWin)) + "\n"
    # print()
    while didIWin and rounds < LIMIT:
        rounds += 1
        result += ("Round " + str(rounds)) + "\n"
        random1 = random2
        guess = makeGuess(random1)
        random2 = randrange(1, 101)
        while random2 == random1:
            random2 = randrange(1, 101)
        correct = correctGuess(random1, random2)
        didIWin = determineWin(guess, correct)
        if didIWin == True:
            wins += 1
        result += "r1 = " + str(random1) + " ----> guess = " + str(guess) + "\n"
        result += "r2 = " + str(random2) + " ----> Guess was " + str(didIWin) + "\n"
        # print()

    # If someone has a 10-streak win, we return True
    if wins == 10:
        print(result)
        return True
    else:
        return False

# MAIN FUNCTION
LIMIT = 10**4
WINS = 0
for i in range(1, LIMIT+1):
    print("**********************************")
    print("Simulation " + str(i))
    simulation = simulate()
    if simulation == True:
        WINS += 1
        print("SUCCESS")
    else:
        print("FAILURE")
    print("**********************************")
    print()

# Statistics
print()
percentage = WINS / LIMIT
percentage = round(100 * percentage, 3)
print("Wins = " + str(WINS))
print("Rounds = " + str(LIMIT))
print("Win percentage = " + str(percentage) + "%")
