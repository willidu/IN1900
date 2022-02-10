import numpy as np
import matplotlib.pyplot as plt


def f(x, t):
    return np.exp(-(x-3*t)**2) * np.sin(3 * np.pi * (x - t))


n = 1000
x = np.linspace(-4, 4, n+1)
y = f(x, 0)

plt.plot(x, y)
plt.xlim(-4, 4)
plt.legend(["np.exp(-(x-3*t)**2) * np.sin(3 * np.pi * (x - t))"])
plt.show()