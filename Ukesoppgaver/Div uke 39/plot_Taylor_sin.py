import matplotlib.pyplot as plt
import numpy as np
from math import factorial


def S(x, n):
    s = 0
    for j in range(n+1):
        s = s + (-1)**j * ((x**(2*j+1)) / factorial(2*j + 1))
    # må bruke s = s + ... istedenfor s += ... pga bug i numpy
    return s


n = 100  # number of points to plot
x = np.linspace(0, 4*np.pi, n)
y = np.sin(x)
y1 = S(x, 1)
y2 = S(x, 2)
y3 = S(x, 3)
y4 = S(x, 6)
y5 = S(x, 12)


plt.plot(x, y, x, y1, x, y2, x, y3, x, y4, x, y5)
plt.legend(["sin(x)", "S(x, 1)", "S(x, 2)", "S(x, 3)", "S(x, 6)", "S(x, 12)"])
plt.ylim(-1.25, 1.25)
plt.xlim(0, 4*np.pi)
plt.grid()
plt.show()
