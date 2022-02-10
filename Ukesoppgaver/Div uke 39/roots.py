import matplotlib.pyplot as plt
import numpy as np


def roots(r, theta, n):
    """r is modulus to complex number
    theta is angle in degrees
    n is number of roots"""

    a = np.zeros(n)
    b = np.zeros(n)

    for k in range(n):
        a[k] = r ** (1/n) * np.cos((theta + 2*np.pi*k)/n)
        b[k] = r ** (1/n) * np.sin((theta + 2*np.pi*k)/n)

    return a, b

x_n_6, y_n_6 = roots(10e-4, 2*np.pi, 6)
plt.plot(x_n_6, y_n_6, "o", label="n = 6")

x_n_12, y_n_12 = roots(10e-4, 2*np.pi, 12)
plt.plot(x_n_12, y_n_12, "o", label="n = 12")

x_n_24, y_n_24 = roots(10e-4, 2*np.pi, 24)
plt.plot(x_n_24, y_n_24, "o", label="n = 24")

plt.title("n-th roots of a  z = 10^−4*e^(i2π)")
plt.axhline(0, color="grey")
plt.axvline(0, color="grey")
plt.xlabel("real component")
plt.ylabel("imaginary component")
plt.legend()
plt.show()
