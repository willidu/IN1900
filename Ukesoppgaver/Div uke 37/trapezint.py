import scipy.integrate as integrate

function = input("Input formula f(x): \n")
code = f"""
def f(x):
    return {function}
"""

import math

exec(code)

a = float(input("a = ? \n"))
b = input("b = ? \n")
if b == "math.pi":
    b = math.pi
else:
    b = float(b)


def trapezint1(f, a, b):
    area = ((b - a) / 2) * (f(a) + f(b))
    return area


v = (integrate.quad(f, a, b))
result = float(v[1])

print(f"Trapezoid approx = {trapezint1(f, a, b)}, error = {abs(result - trapezint1(f, a, b))}")
