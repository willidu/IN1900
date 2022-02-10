from math import sqrt
import sys

a, b, c = sys.argv[1:4]

try:
    a = float(a)
    b = float(b)
    c = float(c)
except ValueError:
    print("Input must be a number")
    exit()

d = b**2 - 4*a*c
if d > 0:
    x1 = (-b + sqrt(d)) / 2 * a
    x2 = (-b - sqrt(d)) / 2 * a
    print(f"x1 = {x1}, x2 = {x2}")
elif d == 0:
    x1 = (-b + sqrt(d)) / 2 * a
    print(f"x = {x1}")
else:
    print("No real roots")

"""
Terminal> python quadratic_roots_cml.py 1 0 -1
x1 = 1.0, x2 = -1.0
"""