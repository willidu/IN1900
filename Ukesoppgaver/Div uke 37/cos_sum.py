import math


def C(x, n):
    s = 1
    term = 1
    for j in range(1, n + 1):
        term = -term * (x ** 2) / (2 * j * (2 * j - 1))
        s += term
    return s


print(f"{abs(math.cos(10 * math.pi) - C(10 * math.pi, 200)):.2e}")
