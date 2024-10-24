from itertools import combinations
from random import shuffle
import operator


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ AUXILIARY FUNCTIONS ~!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Create a class Card
class Card:
    def __init__(self, symbol, value):
        self.symbol = symbol
        self.value = value

# 1. Create the cards
def createCards():
    symbols = ["heart", "diamond", "spade", "club"]
    values = list(range(1, 14))
    cards = list()
    for symbol in symbols:
        for value in values:
            card = Card(symbol, value)
            cards.append(card)
    shuffle(cards)
    shuffle(cards)
    return cards

# 2. Print a list (values)
def valuePrint(cards):
    for card in cards:
        print(card.value)

# 3. Print all the stats of a card
def allPrint(cards):
    string = ""
    for card in cards:
        string += card.symbol + " " + str(card.value) + ", "
    print(string)

# 4. Sort by value
def sortByValue(cards):
    return sorted(cards, key=lambda card: card.value, reverse=True)

# 5. Count the unique values
def uniqueValues(cards):
    sorted_cards = sortByValue(cards)
    uniqueCounter = 1
    uniqueList = [sorted_cards[0]]
    for i in range(1, len(sorted_cards)):
        if sorted_cards[i].value != sorted_cards[i-1].value:
            uniqueCounter += 1
            uniqueList.append(sorted_cards[i])
    # print("Unique values:", uniqueCounter)
    return uniqueCounter #, uniqueList

# 6. Values
def values(cards):
    valuesList = []
    for card in cards:
        valuesList.append(card.value)
    return valuesList

# 7. Symbols
def symbols(cards):
    symbolsList = []
    for card in cards:
        symbolsList.append(card.symbol)
    return symbolsList

# 8. Print all the stats of a card combination
def combinationPrint(combinationString, cards):
    string = combinationString
    for card in cards:
        string += card.symbol + " " + str(card.value) + ", "
    print(string)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ KENTA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~ (6) ~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~~~~~~~

# Kenta (Input = 5 cards)
def isKenta(cards):

    # Bad Cases
    if len(cards) != 5:
        print("No kenta with less or more than 5 cards")
        return False, []
    if uniqueValues(cards) != 5:
        return False, []
    else:
        # Nice and valid cases
        pentada = cards
        valuesPentada = values(pentada)
        unique = uniqueValues(pentada)
        if valuesPentada == [13, 12, 11, 10, 1]:
            return True, pentada
        else:
            if valuesPentada[0] - valuesPentada[4] == 4:
                return True, pentada
    return False, []


# Input = 7 cards
def containsKenta(cards):

    pentades = list(combinations(cards, 5))
    for pentada in pentades:
        pentada = list(pentada)
        flag, kenta = isKenta(pentada)
        if flag == True:
            #print("!!!! There is a kenta !!!!")
            return flag, kenta
    return False, []
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ STRAIGHT FLUSH ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~ (2) ~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~~~~~~~

# Straight Flush (Input = 5 cards)
def isStraightFlush(cards):
    pentada = cards
    flag, kenta = isKenta(pentada)
    if flag == True:
        # Now, I know if this pentada is a kenta and I check the symbols
        pentadaSymbols = symbols(pentada)
        flag2 = True
        for i in range(len(pentadaSymbols)-1):
            if pentadaSymbols[i] != pentadaSymbols[i+1]:
                flag2 = False
                return False, []
        if flag2 == True:
            return True, pentada
    return False, []

# Input = 7 cards
def containsStraightFlush(cards):
    pentades = list(combinations(cards, 5))
    for pentada in pentades:
        pentada = list(pentada)
        flag, straight = isStraightFlush(pentada)
        if flag == True:
            #print("!!!! There is a straight flush !!!!")
            return True, pentada
    return False, []
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FLUSH ROYAL ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~ (1) ~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~~~~~~~

# Flush Royal
def isFlushRoyal(pentada):
    flag, straight = isStraightFlush(pentada)
    if flag == True:
        # It will be flush royal, if the values are [13, 12, 11, 10, 1]
        if values(straight) == [13, 12, 11, 10, 1]:
            print("YEAH")
            return True, straight
    return False, []

def containsFlushRoyal(cards):
    pentades = list(combinations(cards, 5))
    for pentada in pentades:
        pentada = list(pentada)
        flag, flush = isFlushRoyal(pentada)
        if flag == True:
            #print("!!!! There is a flush royal !!!!")
            return True, pentada
    return False, []

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FLUSH ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~ (5) ~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~~~~~~~

# Full house (input = 5 cards)
def isFlush(pentada):
    if len(pentada) != 5:
        print("Error while using function '", isFlush.__name__, "'")
        return "-1000", "-1000"
    else:
        pentadaSymbols = symbols(pentada)
        flag2 = True
        for i in range(len(pentadaSymbols) - 1):
            if pentadaSymbols[i] != pentadaSymbols[i + 1]:
                flag2 = False
                return False, []
        if flag2 == True:
            return True, pentada

# Input = 7 cards
def containsFlush(cards):
    pentades = list(combinations(cards, 5))
    for pentada in pentades:
        pentada = list(pentada)
        flag, flush = isFlush(pentada)
        if flag == True:
            #print("!!!! There is a flush !!!!")
            return True, pentada
    return False, []
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ KARE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~ (3) ~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~~~~~~~

# Kare (Input = 4 cards)
def isKare(tetrada):
    if len(tetrada) != 4:
        print("Error while using function '", isKare.__name__, "'")
        return "-1000", "-1000"
    else:
        valuesTetrada = values(tetrada)
        flag = True
        for i in range(len(valuesTetrada)-1):
            if valuesTetrada[i] != valuesTetrada[i+1]:
                flag = False
                return False, []
        if flag == True:
            return True, tetrada

# Input = 7 cards
def containsKare(cards):
    tetrades = list(combinations(cards, 4))
    for tetrada in tetrades:
        tetrada = list(tetrada)
        flag, kare = isKare(tetrada)
        if flag == True:
            # print("!!!! There is a kare !!!!")
            return True, kare
    return False, []

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FULL HOUSE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~ (4) ~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~~~~~~~

# Full House (Input = 5 cards)
def isFullHouse(pentada):
    if len(pentada) != 5:
        print("Error while using function '", isFullHouse.__name__, "'")
        return "-1000", "-1000"

    v = values(pentada)
    # I want 3 values equal and 2 values equal (remember that this list is sorted)
    # Sth in this form: [12, 12, 12, 5, 5] or [12, 12, 5, 5, 5]
    if (v[0] == v[1]) and (v[3] == v[4]) and ((v[2] == v[1]) or (v[2] == v[3])):
        return True, pentada
    return False, []

# Input = 7 cards
def containsFullHouse(cards):
    pentades = list(combinations(cards, 5))
    for pentada in pentades:
        pentada = list(pentada)
        flag, full = isFullHouse(pentada)
        if flag == True:
            # print("!!!! There is a flush !!!!")
            return True, pentada
    return False, []


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TRIFYLLIA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~ (7) ~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~~~~~~~

# Trifyllia (Input = 3 cards)
def isTrifyllia(triada):
    if len(triada) != 3:
        print("Error while using function '" + isTrifyllia.__name__ + "'")
        return "-1000", "-1000"
    v = values(triada)
    if v[0] == v[1] and v[1] == v[2]:
        return True, triada
    return False, []

# Input = 7 cards
def containsTrifyllia(cards):
    triades = list(combinations(cards, 3))
    for triada in triades:
        triada = list(triada)
        flag, trifyllia = isTrifyllia(triada)
        if flag == True:
            # print("!!!! There is a trifyllia !!!!")
            return True, triada
    return False, []

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TWO PAIRS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~ (8) ~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~~~~~~~

# Two pairs (Input - 4 cards)
def isPairs(tetrada):
    if len(tetrada) != 4:
        print("Error while using function '" + isPairs().__name__ + "'")
        return "-1000", "-1000"
    v = values(tetrada)
    if v[0] == v[1] and v[2] == v[3] and v[1] != v[2]:
        return True, tetrada
    return False, []

# Input = 7 cards
def containsPairs(cards):
    tetrades = list(combinations(cards, 4))
    for tetrada in tetrades:
        tetrada = list(tetrada)
        flag, pairs = isPairs(tetrada)
        if flag == True:
            # print("!!!! There are 2 pairs !!!!")
            return True, tetrada
    return False, []



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DIFYLLIA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~ (9) ~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~~~~~~~

# Difyllia (Input = 2 cards)
def isDifyllia(diada):
    if len(diada) != 2:
        print("Error while using function '" + isTrifyllia.__name__ + "'")
        return "-1000", "-1000"
    v = values(diada)
    if v[0] == v[1]:
        return True, diada
    return False, []

# Input = 7 cards
def containsDifyllia(cards):
    diades = list(combinations(cards, 2))
    for diada in diades:
        diada = list(diada)
        flag, difyllia = isDifyllia(diada)
        if flag == True:
            # print("!!!! There is a difyllia !!!!")
            return True, diada
    return False, []

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Testing functions
def testing(sorted_first7):

    print()
    print("**********************************************************************")
    allPrint(sorted_first7)
    print("**********************************************************************")
    testing(sorted_first7)

    # 1. Testing Flush Royal
    flag, royal = containsFlushRoyal(sorted_first7)
    print("1. Contains Flush Royal?", flag)
    combinationPrint("Flush royal is:", royal)
    print()
    # 2. Testing Straight Flush
    flag, straight = containsStraightFlush(sorted_first7)
    print("2. Contains Straight Flush?", flag)
    combinationPrint("Straight Flush is:", straight)
    print()
    # 3. Testing Kare
    flag, kare = containsKare(sorted_first7)
    print("3. Contains Kare?", flag)
    combinationPrint("Flush is:", kare)
    print()
    # 4. Testing Full House
    flag, full = containsFullHouse(sorted_first7)
    print("4. Contains Full House?", flag)
    combinationPrint("Full House is:", full)
    print()
    # 5. Testing Flush
    flag, flush = containsFlush(sorted_first7)
    print("5. Contains Flush?", flag)
    combinationPrint("Flush is:", flush)
    print()
    # 6. Testing Kenta
    flag, kenta = containsKenta(sorted_first7)
    print("6. Contains Kenta?", flag)
    combinationPrint("Kenta is:", kenta)
    print()
    # 7. Testing Trifyllia
    flag, trifyllia = containsTrifyllia(sorted_first7)
    print("7. Contains Trifyllia?", flag)
    combinationPrint("Trifyliia is:", trifyllia)
    print()
    # 8. Testing Pairs
    flag, pairs = containsPairs(sorted_first7)
    print("8. Contains pairs?", flag)
    combinationPrint("Pairs are:", pairs)
    print()
    # 9. Testing Trifyllia
    flag, difyllia = containsDifyllia(sorted_first7)
    print("9. Contains Difyllia?", flag)
    combinationPrint("Difyliia is:", difyllia)
    print()



# DETERMINE BIGGEST COMBINATION
def determine(sorted_first7):

    allPrint(sorted_first7)
    index = 0

    # Begin the process of searching

    # 1. Flush Royal
    flag, winner_comb = containsFlushRoyal(sorted_first7)
    if flag == True:
        print("        FLUSH ROYAL")
        return index
    index += 1
    # 2. Straight Flush
    flag, winner_comb = containsStraightFlush(sorted_first7)
    if flag == True:
        print("        STRAIGHT FLUSH")
        return index
    index += 1

    # 3. Kare
    flag, winner_comb = containsKare(sorted_first7)
    if flag == True:
        print("        Kare")
        return index
    index += 1
    # 4. Full House
    flag, winner_comb = containsFullHouse(sorted_first7)
    if flag == True:
        print("        FULL HOUSE")
        return index
    index += 1

    # 5. Flush
    flag, winner_comb = containsFlush(sorted_first7)
    if flag == True:
        print("        FLUSH")
        return index
    index += 1
    # 6. Kenta
    flag, winner_comb = containsKenta(sorted_first7)
    if flag == True:
        print("        KENTA")
        return index
    index += 1

    # 7. TRIFYLLIA
    flag, winner_comb = containsTrifyllia(sorted_first7)
    if flag == True:
        print("        Trifyllia")
        return index
    index += 1
    # 8. 2 Pairs
    flag, winner_comb = containsPairs(sorted_first7)
    if flag == True:
        print("        2 Pairs")
        return index
    index += 1
    # 9. Difyllia
    flag, winner_comb = containsDifyllia(sorted_first7)
    if flag == True:
        print("        Difyllia")
        return index
    index += 1
    # 10. High Card
    print("        High Card")
    return index







# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~~~~~~~~~~ MAIN FUNCTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Create data for storing each winner combination
# Flush royal(1) goes in index 0, straight flush(2) in 2, ...., difyllia(9) goes in 8, high card(10) goes in 9
named_combinations = [" Flush Royal  ", "Straight Flush", "     Kare     ", "  Full House  ", "    Flush     ", "    Kenta     ", "  Trifyllia   ", "   2 Pairs    ", "   Difyllia   ", "  High Card   "]
winner_combinations = [0 for i in range(10)]
N = 10**5
for round in range(1, N+1):
    print("~~~~~~~~ Round " + str(round) + " ~~~~~~~~")
    cards = createCards()
    first7 = cards[0:7]
    sorted_first7 = sortByValue(first7)
    index = determine(sorted_first7)
    winner_combinations[index] += 1
    print()

# Print Stats
print()
print("~~~~~~~~ Winner Combinations List ~~~~~~~~")
print(winner_combinations)
print()
for i in range(len(winner_combinations)):
    named = named_combinations[i]
    times_won = winner_combinations[i]
    percentage100 = 100 * (times_won / N)
    print(named + ": " + str(times_won) + " wins  =  " + str(percentage100) + "%")