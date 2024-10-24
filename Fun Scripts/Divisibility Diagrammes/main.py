from matplotlib import pyplot as plt

# Function 1 - Find the divisors of all the numbers in a given range (start, end + 1)
def findDivisors(start, end):
    all_divisors = list()
    for n in range(start, end + 1):
        divisors = list()
        divisors.append(1)
        if n <= 1 or n != int(n):
            print("Error while using function '" + findDivisors.__name__ + "'")
            divisors.append(0)
        else:
            for i in range(2, int(n/2 + 1)):
                if n % i == 0:
                    divisors.append(i)
            divisors.append(n)
        all_divisors.append(divisors)
    return all_divisors


# Function 2 - Produce 2 plots
def produce_plots(start, end, all_divisors):
    x = list()
    y1 = list()
    y2 = list()
    primes = list()
    for arr in all_divisors:
        LEN = len(arr)
        n = arr[LEN - 1]
        x.append(n)
        y1.append(LEN)
        y2.append(n / LEN)
        if LEN == 2:
            primes.append(n)

    print(" Numbers = " + str(x))
    print("Divisors = " + str(all_divisors))
    print()
    print("        Numbers = " + str(x))
    print("Num of divisors = " + str(y1))
    print("   Divisibility = " + str(y2))
    print("Primes = " + str(primes))
    print()
    avg_divisors = sum(y1) / len(y1)
    avg_divisibility = sum(y2) / len(y2)
    print("\t******** Range = [" + str(start) + ", " + str(end) + "] ********")
    print("Average num of divisors = " + str(avg_divisors))
    print("   Average divisibility = " + str(avg_divisibility))

    plt.plot(x, y1)
    plt.xlabel('x')
    plt.ylabel('# of divisors')
    plt.title("Number of divisors")
    plt.show()
    plt.plot(x, y2)
    plt.xlabel('x')
    plt.ylabel('Divisibility')
    plt.title("Divisibility")
    plt.show()


# MAIN FUNCTION
start = 2
end = 10**3
all_divisors = findDivisors(start, end)
produce_plots(start, end, all_divisors)
