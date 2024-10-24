def countCollageTerms(n):
    # Counter = 1, because we also count the first number "n" in the chain
    counter = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
            counter += 1
        else:
            n = 3 * n + 1
            counter += 1
    return counter

# MAIN FUNCTION
from timeit import default_timer as timer

LIMIT = 10**5
collatz = 0
maxSequenceChain = 0
start = timer()
for n in range(1, LIMIT):
    value = countCollageTerms(n)
    print(str(n) + " ---> " + str(value) + " terms.")
    if value > maxSequenceChain:
        collatz = n
        maxSequenceChain = value

end = timer()
print()
print("********  EXECUTION TIME UNTIL " + str(LIMIT) + " = " + str(1000*(end-start)) + "ms  ********")
print("From 1 to " + str(LIMIT) + " the number with the longest Collatz sequence is: " + str(collatz) + ". It contains " + str(maxSequenceChain) + " numbers.")