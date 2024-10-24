from copy import deepcopy


# Function 1 - Break intergers into his digits
def break_digits(n):
    temp = [str(element) for element in str(n)]
    card = [int(element) for element in temp]
    return card


# Function 2 - Reversing and doubling
def double(card):
    LEN = len(card)
    card.reverse()
    # 1. Doubling the elements from the second-to-last-digit and moving to the left
    # 2. Checking if it is 2-digit number: If yes, add the digits (or % 9)
    for i in range(1, LEN, 2):
        card[i] = 2 * card[i] % 9
    card.reverse()
    return card


# Function 3 - Checking if it is valid
def check_valid(card):
    S = sum(card) % 10
    if S == 0:
        return True, S
    else:
        return False, S


# Function 4 - Propose solution
def propose_correct(card, S):
    last = card[len(card) - 1]
    extra = 10 - S
    correct_last = (last + extra) % 10
    print("If the last digit is changed from " + str(last) + " to " + str(
        correct_last) + ", we will have a valid card number.")
    return correct_last


# Function 5 - Simulate
def Luhn(CARD):
    card = break_digits(CARD)
    initial_card = deepcopy(card)
    # print("Initial card = " + str(initial_card))
    new_card = double(card)
    # print("New card = " + str(new_card))
    flag, S = check_valid(new_card)
    if flag:
        print(str(initial_card) + " = VALID")
    else:
        print(str(initial_card) + " = INVALID")
        correct_last = propose_correct(new_card, S)
        correct = deepcopy(initial_card)
        correct[len(card) - 1] = correct_last
        print(str(correct) + " =  VALID")


# MAIN FUNCTION
CARD1 = 5146713835430
Luhn(CARD1)
print()
CARD2 = 5146713835435
Luhn(CARD2)