import turtle
from math import pi
try:
    # import version included with old SymPy
    from sympy.mpmath import mp
except ImportError:
    # import newer version
    from mpmath import mp

# 1. Decimal places = 1000
mp.dps = 3 * 10**3
_PI_ = mp.pi
PI = [int(element) for element in str(_PI_) if element != "."]
print(PI)

# 2. Settings
turtle.speed(100)
turtle.color("red")
walk = 10
basis = 10
angle = 360 / basis
counter = 0

# Algorithm
for digit in PI:
    counter += 1
    print("Counter = " + str(counter) + ", digit = " + str(digit) + ", angle = " + str(digit * angle))
    turtle.left(digit * angle)
    turtle.forward(walk)
