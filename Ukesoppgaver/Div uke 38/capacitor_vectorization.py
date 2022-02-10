import numpy as np
import matplotlib.pyplot as plt


def I(t, R, C, V0):
    return C * V0 * np.exp(- t / (R * C))


V0 = 50.0
R = 350.0
C = 0.007

t = 10
n = 1000
dt = float(t) / n

t_list = []
I_list = []
for i in range(n):
    t_list.append(dt * i)
    I_list.append(I(t_list[i], R, C, V0))

x = np.linspace(0, t, n)
y = I(x, R, C, V0)


plt.plot(t_list, I_list, x, y)
plt.show()
