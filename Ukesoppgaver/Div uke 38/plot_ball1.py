import numpy as np
import matplotlib.pyplot as plt

v_0 = 10.0
g = 9.81

n = 100
t0 = 0
t_max = 2 * v_0 / g
dt = t_max / n

x = np.linspace(0, t_max, n)
y = np.zeros(n)
for i in range(n):
    y[i] = v_0 * x[i] - 0.5 * g * x[i] ** 2

plt.plot(x, y)
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.axis(xmin=0, xmax=2.1, ymin=0)
plt.grid()
plt.legend(["y(t)"])
plt.show()
