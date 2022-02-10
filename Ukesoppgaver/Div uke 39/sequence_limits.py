import math
import matplotlib.pyplot as plt
import numpy as np

N = 100
a = [0] * (N + 1)

for n in range(N + 1):
    nominator = 7 + 1 / (n + 1)
    denominator = 3 - 1 / ((n + 1) ** 2)
    a[n] = nominator / denominator
    error = abs(7 / 3 - a[n]) / abs(a[n])
    # print(f"{n:3} {a[n]:12}    error = {error:e}")

"""Observes that the error decreases for larger N"""

N = 1000
b = [0] * (N + 1)
for n in range(N + 1):
    nominator = math.sin(2 ** (-n))
    denominator = 2 ** (-n)
    b[n] = nominator / denominator
    # print(n, b[n], nominator, denominator)

"""b[n] -> 1.0 når n -> 1000"""


def d(f, x, N):
    D = np.zeros(N+1)
    for n in range(N+1):
        h = 2 ** (-n)
        D[n] = (f(x + h) - f(x)) / h
    return D

D1 = d(np.sin, 0, 80)
D2 = d(np.sin, np.pi, 80)
n = np.arange(81)

plt.plot(n, D1, "o")
plt.plot(n, D2, "o")
plt.xlabel("n")
plt.ylabel("Dn")
plt.legend(["x = 0", "x = pi"])
plt.show()

"""
Would expect derivative of sin(pi) to be -1. 
With large n values h becomes very very small.
An approximation is therefore f(x)-f(x) which is zero.
"""