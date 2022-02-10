import matplotlib.pyplot as plt
import numpy as np

def y(t, A, gamma, k, m):
    return A*np.exp(-gamma*t)*np.cos(np.sqrt(k/m)*t)

n = 101

t_array_a = np.zeros(n)
y_array_a = np.zeros(n)
dt = 25 / (n-1)
for i in range(n):
    t_array_a[i] = i * dt
    y_array_a[i] = y(t_array_a[i], k=4, gamma=0.15, m=9, A=-0.3)

t_array_b = np.linspace(0, 25, n)
y_array_b = y(t_array_b, k=4, gamma=0.15, m=9, A=-0.3)

plt.plot(t_array_a, y_array_a, color="red")
plt.plot(t_array_b, y_array_b, "-.")
plt.grid()
plt.xlim(0, 25)
plt.legend(["y(t) for-loop", "y(t) vectorized"])
plt.xlabel("time (seconds)")
plt.ylabel("height (m)")
plt.show()

"""
Ser at begge settene med arrays plotter samme linje.
"""