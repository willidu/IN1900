import matplotlib.pyplot as plt
import numpy as np

F = 100000  # Fortune
p = 3.5 # annual interest rate %
q = 36
n = 10 # years
I = 2.5  # Inflation %
# c is consumption each year

x = [F]
c = [(F * (p*q)/(10**4))]
for i in range(len(x), n):
    x.append(x[i-1] + (x[i-1] * (p/100)) - c[i-1])
    c.append(c[i-1] + (c[i-1] * (I/100)))

x_n = [0] * len(x)
for i in range(len(x)):
    x_n[i] = x[i] - c[i]

n_val = np.linspace(0, 10, 10)
plt.plot(n_val, x_n, n_val, x)
plt.xlim(0, n)
plt.show()