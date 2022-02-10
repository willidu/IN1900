import sys
import numpy as np
import matplotlib.pyplot as plt

print(sys.argv)
v = []
for i in range(1, len(sys.argv)):
    v.append(float(sys.argv[i]))
print(v)


def height(v):
    g = 9.81
    n = 100
    t_max = 2 * v / g
    x_val = np.linspace(0, t_max, n)
    y_val = np.zeros(n)
    for i in range(n):
        y_val[i] = v * x_val[i] - 0.5 * g * x_val[i] ** 2
    return [x_val, y_val]


x = []
y = []

for i in range(len(v)):
    vel = v[i]
    func = height(vel)
    x.append(func[0])
    y.append(func[1])

max_t = 0
max_y = 0

for i in range(len(x)):
    if max(x[i]) > max_t:
        max_t = max(x[i])
        m = max_t + max_t * 0.05
    if max(y[i]) > max_y:
        max_y = max(y[i])
        n = max_y + max_y * 0.05
    plt.plot(x[i], y[i], label=f"v0 = {v[i]}")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.axis(xmin=0, xmax=m, ymin=0, ymax=n)
plt.grid()
plt.legend()
plt.show()

# Kjør i terminal med sysarg f eks 3 4 5