import matplotlib.pyplot as plt
import numpy as np

n = 100
x = np.linspace(-20, 120, n + 1)

y1 = (x - 30) / 2  # approximation
y2 = (x - 32) * 5/9  # more accurate

plt.plot(x, y1, x, y2)
plt.xlabel("Fahrenheit")
plt.ylabel("Celsius")
plt.xlim(-20, 120)
plt.legend(["(F-30)/2", "(F-32) * 5/9"])
plt.grid()
plt.show()
