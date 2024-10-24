'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
'''


'''
CHAPTER 1 - CREATE THE PRIMES LIST
'''
import itertools
from timeit import default_timer as timer
from itertools import permutations
from math import pow

LIMIT = int(pow(10, 5))
primes = [2]
start = timer()
for i in range(3, LIMIT):
    isIPrime = True
    for prime in primes:
        if i % prime == 0:
            isIPrime = False
            break
    if isIPrime == True:
        primes.append(i)

end = timer()
timeInMillisForPrimes = 1000 * (end - start)
print()

print("************************    PRIMES    ************************")
print("I found " + str(len(primes)) + " primes in the range (1, " + str(LIMIT) + ").")
print("These primes are: " + str(primes))
print("~~~~ Time needed for primes: " + str(timeInMillisForPrimes) + " ms ~~~~")



'''
CHAPTER 2 - AUXILIARY FUNCTION - FACTORIAL
'''
def factorial(n):
    if n < 0 or int(n) != n:
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)


'''
CHAPTER 3 - ISCIRCULAR FUNCTION
'''
def isCircular(number, primes):
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!
    # This line can be subtracted
    if number not in primes:
        print(str(number) + " cannot be circular prime, because it isn't a prime number")
        return None
    # So, number is prime
    # All the primes with one digit (2, 3, 5, 7) are circular
    if number / 10 < 1:
        return True
    else:
        # Number is a 2,3,4,....-digit prime
        # Convert it into a string
        # Example with
        # 0. number = 137
        stringNumber = str(number)
        # 1. stringNumber = "137"
        listString = [stringNumber[i] for i in range(len(stringNumber))]
        # 2. listString = ["1", "3", "7"]
        intString = list()
        for i in range(len(listString)):
            try:
                intString.append(int(listString[i]))
            except ValueError:
                return None
        # 3. intString = [1, 3, 7]
        n = len(intString)          # n = 3
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        perms = list(permutations(intString))
        # 4. perms = [(1, 3, 7), (1, 7, 3), (3, 1, 7), (3, 7, 1), (7, 1, 3), (7, 3, 1)]
        permNumbers = []
        for i in range(factorial(n)):
            permNumber = 0
            for j in range(n):
                permNumber += perms[i][j] * pow(10, n-1-j)
            permNumbers.append(int(permNumber))
        # 5. permNumbers = [137, 173, 317, 371, 713, 731]

        # Time to check
        flag = True
        for permNumber in permNumbers:
            if permNumber not in primes:
                return False
        return True


'''
CHAPTER 4 - MAIN FUNCTION
'''

# MAIN FUNCTION
circulars = []
start2 = timer()
for prime in primes:
    if isCircular(prime, primes) == True:
        circulars.append(prime)
end2 = timer()
timeInMillisForCirculars = 1000 * (end2 - start2)

print()
print("************************    CIRCULARS    ************************")
print("I found " + str(len(circulars)) + " circular primes in the range (1, " + str(LIMIT) + ").")
print("These numbers are: " + str(circulars))
print("~~~~ Time needed for circulars: " + str(timeInMillisForCirculars) + "ms ~~~~")
