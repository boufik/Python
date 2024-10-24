# I will try to approach a function with a Taylor series that has N-rank (3-rank here)
# My function will be:
# f(x) = sin(x) + 2 * ln(x+1) - 3 * x ^ 3 in the interval [0, 4*pi]
from math import pi, sin, cos, log
from matplotlib import pyplot as plt

def f(x):
    return sin(x) + 2 * log(x+1) - 3 * x**3

def df(x):
    return cos(x) + 2 / (x+1) - 9 * x**2

def d2f(x):
    return - sin(x) - 2 / (x+1)**2 - 18 * x

def d3f(x):
    return - cos(x) + 4 / (x+1)**3 - 18

def taylorF(x, center):
    return f(center) + df(center) * (x-center) + 1/2 * d2f(center) * (x-center)**2 + 1/6 * d3f(center) * (x-center)**3


# MAIN FUNCTION
x = list()
counter = 0
while counter <= 4*pi:
    x.append(counter)
    counter += pi / 100

centers = list(range(0, 11, 2))
for center in centers:
    function = list()
    taylor = list()
    for elementX in x:
        function.append(f(elementX))
        taylor.append(taylorF(elementX, center))
    plt.plot(x, function, label="Function")
    plt.plot(x, taylor, label="Taylor")
    plt.title("Center = " + str(center))
    plt.legend()
    plt.show()