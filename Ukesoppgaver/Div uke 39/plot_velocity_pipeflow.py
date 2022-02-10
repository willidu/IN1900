import matplotlib.pyplot as plt
import numpy as np

def v(r, beta, my, R, n):
    return (beta / 2*my)**(1/n) * (n / (n+1)) * (R**(1 + 1/n) - r**(1 + 1/n))

N = 100  # number of points
r = np.linspace(0, 1, N)
v1 = v(r, R=1, beta=0.02, my=0.02, n=0.1)

plt.plot(r, v1)
plt.grid()
plt.xlim(0, 1)
plt.xlabel("r, distance from center of pipe (m)")
plt.ylabel("velocity (m/s)")
plt.title("Velocity profile for pipeflow")

# Sub n for f
f = 1
lines = plt.plot(r, v(r, n=1, R=1, beta=0.02, my=0.02))
while f >= 0.01:
    plt.legend(["v(r)", "v(r) var. n"])
    lines[0].set_ydata(v(r, n=f, R=1, beta=0.02, my=0.02))
    v_0 = v(0, n=f, R=1, beta=0.02, my=0.02)
    plt.ylim(0, v_0)
    plt.draw()
    plt.pause(0.1)
    f -= 0.01

"""
Kjør fra terminal så funker animasjonen :)
Normalisering slik at v(0) er lik?
"""