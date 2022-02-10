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
        a = input("Input a value for a = ")
    try:
        b = float(b)
    except (NameError, ValueError) as error:
        b = input("Input a value for b = ")
    try:
        c = float(c)
    except (NameError, ValueError) as error:
        c = input("Input a value for c = ")
finally:
    a = float(a)
    b = float(b)
    c = float(c)


def roots(a, b, c):
    d = b**2 - 4*a*c
    try:
        r_d = sqrt(d)
    except ValueError:
        print("Square root of negative number not allowed")
        exit()
    if d > 0:
        x1 = -b + sqrt(d) / 2 * a
        x2 = -b - sqrt(d) / 2 * a
        print(f"x1 = {x1}, x2 = {x2}")
    elif d == 0:
        x1 = -b + sqrt(d) / 2 * a
        print(f"x = {x1}")


roots(a, b, c)

"""
Terminal> python quadratic_roots_error2. py 1 0
Input must be three numbers
a = ?
1
b = ?
0
c = ?
1
Square root of negative number not allowed
"""