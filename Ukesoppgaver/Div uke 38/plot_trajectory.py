import sys
import numpy as np
import matplotlib.pyplot as plt

g = 9.81
# initial height, angle and initial velocity
y0, theta, v0 = (sys.argv[1:4])
y0 = float(y0)
theta = float(theta)
v0 = float(v0)


def f(x):
    return x*np.tan(theta) - ((g * x**2) / (2 * v0**2 * (np.cos(theta))**2)) + y0


n = 100
x = np.linspace(0, 15, n)
y = f(x)

plt.plot(x, y)
plt.xlim(0)
plt.ylim(0)
plt.xlabel("x-coordinate")
plt.ylabel("y-coordinate")
plt.grid()
plt.show()

"""
Terminal> python plot_trajectory.py 10 45 10
See graph. 
"""