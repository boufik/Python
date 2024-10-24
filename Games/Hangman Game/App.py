from timeit import default_timer as timer
from random import randrange


# Function 1
def writeProgress(letters, foundLetters):
    result = ""
    for i in range(len(foundLetters)):
        if foundLetters[i] == 1:
            result += letters[i] + " "
        else:
            result += "- "
    return result


# 1. Python program to read file word by word
# Opening the text file
words = list()
with open('words.txt', 'r') as file:
    for line in file:
        for word in line.split():
            words.append(word)

# print(words)
# print("There are " + str(len(words)) + " words")
print()
print("*********************************************************************************")
print("*********************************************************************************")
print("Welcome to the 'Hangman Game'. You will have to make 2 choices to start the game.")
for i in range(100):
    # 2. Take the user's choices as data
    attempts = int(input("1. How many attempts do you want to have? "))
    while attempts <= 0 or attempts > 25 or attempts != int(attempts):
        incorrect = int(input("1. How many incorrect answers do you want to have? "))
    NLimit = int(input("2. What minimum word length do you want? "))
    while NLimit < 4 or NLimit > 16:
        NLimit = int(input("2. What minimum word length do you want? "))

    # 3. Randomize the word according to given criteria
    word = words[randrange(0, len(words))]
    # print(word)
    while len(word) < NLimit:
        word = words[randrange(0, len(words))]
        # print(word)


    # 4. Let the game begin
    print()
    # print(word)
    letters = [word[i].lower() for i in range(len(word))]
    # I will make a list in which I match each letter with 0 or 1
    # The element will be 0 if this letter is not revealed yet
    foundLetters = [0 for _ in range(len(letters))]
    print("Your word is ready and has " + str(len(word)) + " letters.")
    print(writeProgress(letters, foundLetters))
    attemptsRemaining = attempts
    print("Attempts reamining: " + str(attemptsRemaining))

    # 5. While loop
    print()
    print()
    counter = 0
    lettersGuessed = list()
    wordFound = False

    while attemptsRemaining > 0 and wordFound == False:
        counter += 1
        print("~~~~~~~~~~~~~~~~ Round " + str(counter) + " ~~~~~~~~~~~~~~~~")
        print("    Used letters = " + str(lettersGuessed))
        letterGuessed = input("Guess a letter: ")
        # a) First, I will check if the user has guessed this letter again. I will give him 1 more chance.
        for i in range(len(lettersGuessed)):
            if letterGuessed == lettersGuessed[i]:
                print("You guessed this letter (" + letterGuessed + ") again. I you do it again, I will count it as 'fault'.")
                letterGuessed = input("Now, try to guess another letter: ")
                break
        lettersGuessed.append(letterGuessed)
        # b) Now, we have a valid try/guess for the next letter and we have to check if this letter
        # exists in ouy random word
        exists = False
        for i in range(len(letters)):
            if letterGuessed == letters[i]:
                foundLetters[i] = 1
                exists = True
                # I won't break here, because maybe 1 letter exists more than once
        # c) Last step is to reduce the remaining attempts in case of a wrong guess
        if exists == False:
            attemptsRemaining -= 1
            print(letterGuessed + " is NOT in our word.")
        else:
            print(letterGuessed + " is IN our word.")
        # d) Check if I have found the word
        found = True
        for i in range(len(foundLetters)):
            if foundLetters[i] == 0:
                found = False
                break
        wordFound = found
        # e) Show the progress of the word's guesses
        print(writeProgress(letters, foundLetters))
        print("Attempts remaining: " + str(attemptsRemaining))
        print()

    if attemptsRemaining == 0:
        print()
        print("You failed to guess the word correctly, but your try was a good one.")
        print("The word was ----> " + str(word))
    else:
        print()
        print("Congratulations!!!!")
        print("You made " + str(attempts - attemptsRemaining) + "/" + str(attempts) + " faults and found the correct word")
        print("The word was ----> " + str(word))
    print()