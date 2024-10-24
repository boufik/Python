try:
    # import version included with old SymPy
    from sympy.mpmath import mp
except ImportError:
    # import newer version
    from mpmath import mp

# Decimal places = 1000
LIMIT = 3000
mp.dps = LIMIT
_PI_ = mp.pi
PI = [int(element) for element in str(_PI_) if element != "."]

for ROUND in range(100):
    print(80 * "*")
    # Ask the user to give an input to be checked
    sequence = input("Which number sequence do you want me to search if it exists in 'pi'? ")
    target = [int(element) for element in str(sequence)]
    LEN = len(target)
    index = -1000
    for i in range(len(PI) - len(target)):
        if PI[i : i+LEN] == target:
            index = i
            break
    if index == -1000:
        print("Sequence " + sequence + " does not exist in the first " + str(LIMIT) + " digits of pi.")
    else:
        print("Sequence " + sequence + " exists in pi located from index " + str(index) + " to index " + str(index + LEN - 1))
    print()