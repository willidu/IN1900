import matplotlib.pyplot as plt
import numpy as np

class F:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def __call__(self, x):
        return np.sin(self.n*x)*np.cos(self.m*x)

u = F(0.3, 6.9)
v = F(7, np.pi)

x = np.linspace(0, 2*np.pi, 1000)

plt.plot(u(x), v(x))
plt.show()

"""
Terminal> python F.py
Plotter en merkelig graf men funker
"""