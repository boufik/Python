'''
4/n = 1/i + 1/j + 1/k
n > 1 <----> 4/n <= 2 <----> i=1, j=2, k=2 the lower bounds
'''

# FUNCTION 1 - Egyptian fractions
def egyptian(n, LIMIT):
    if n <= 1 or n != int(n):
        print("Error while using function '" + egyptian.__name__ + "'")
        return -1000
    isThereSolution = False
    for i in range(1, LIMIT+1):
        flag1 = False
        for j in range(2, LIMIT+1):
            flag2 = False
            for k in range(2, LIMIT+1):
                if 4/n == 1/i + 1/j + 1/k:
                    flag1 = True
                    flag2 = True
                    flag3 = True
                    isThereSolution = True
                    print("4/" + str(n) + " = " + "1/" + str(i) + " + 1/" + str(j) + " + 1/" + str(k))
                    break       # This one will drop me in 2nd loop
            if flag2:
                break
        if flag1:
            break
    if isThereSolution == False:
        print(str(n) + ": 4/" + str(n) + " cannot be written as sum of 3 egyptian fractions! LIMIT = " + str(LIMIT) + " (lowest = 1/" + str(LIMIT) + ")")
    # With the 3 break-cases, we will gain much time

# MAIN FUNCTION
# First, I will decide for the LIMIT
LIMIT = 200
for n in range(2, 100):
    egyptian(n, LIMIT)