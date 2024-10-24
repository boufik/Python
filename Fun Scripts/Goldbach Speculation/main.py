# Function 1 - Find the primes
def findPrimes(limit):
    primes = [2, 3]
    for n in range(4, limit+1):
        isPrime = True
        for prime in primes:
            if n % prime == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(n)
    print("Primes until " + str(limit) + " ----> " + str(primes))
    print()
    return primes

# FUNCTION 2 - Goldbach
def goldbach(limit):
    primes = findPrimes(limit)
    for n in range(4, limit, 2):
        isThereASum = False
        for prime1 in primes:
            for prime2 in primes:
                if n == prime1 + prime2:
                    isThereASum = True
                    print(str(n) + " = " + str(prime1) + " + " + str(prime2))
                    break
        if isThereASum == False:
            print("Error with number " + str(n) + ". Cannot find 2 primes with sum = " + str(n))
            break


# MAIN FUNCTION
limit = 10**4
goldbach(limit)