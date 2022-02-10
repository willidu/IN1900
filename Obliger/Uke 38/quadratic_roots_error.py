from math import sqrt
import sys

try:
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
except IndexError:
    try:
        a = float(a)
    except (NameError, ValueError) as error:
        a = input("Input a value for a = \n")
    try:
        b = float(b)
    except (NameError, ValueError) as error:
        b = input("Input a value for b = \n")
    try:
        c = float(c)
    except (NameError, ValueError) as error:
        c = input("Input a value for c = \n")
finally:
    a = float(a)
    b = float(b)
    c = float(c)

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
Terminal> python quadratic_roots_error.py 1 to
Input a value for b =
0
Input a value for c =
-1
x1 = 1.0, x2 = -1.0
"""