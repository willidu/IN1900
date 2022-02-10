import sys
import numpy as np
import matplotlib.pyplot as plt

m = float(sys.argv[1])
v0 = float(sys.argv[2])
g = 9.81
n = 100  # number of points
t = np.linspace(0, 2*v0/g, n)

def y(t, v0):
    return v0*t - 0.5*g*t**2

P_array = m*g*y(t, v0)
K_array = 0.5*m*((v0 - g*t)**2)
energy_total = P_array + K_array

plt.plot(t, P_array, t, K_array, t, energy_total)
plt.legend(["Potential energy", "Kinetic energy", "Total energy"])
plt.xlim(0)
plt.ylim(0)
plt.grid()
plt.show()
