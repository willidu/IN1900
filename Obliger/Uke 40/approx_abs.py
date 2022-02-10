import numpy as np
import matplotlib.pyplot as plt

def abs_approx(x, N):
    s = 0
    for n in range(1, N+1):
        s += (np.cos((2*n-1)*x))/((2*n-1)**2)
    return np.pi/2 - 4/np.pi * s

x = np.linspace(-np.pi, np.pi, 100)
for n in range(1, 5):
    plt.plot(x, abs_approx(x, n), label=f'N={n}')

plt.xlim(-np.pi, np.pi)
plt.ylim(0, None)
plt.title("Approximation of f(x) = |x|")
plt.legend(loc='lower right')
plt.grid()
plt.show()

"""
Terminal> python approx_abs.py
Plotter en finfin graf
"""