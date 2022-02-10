import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 2, 20)
y1 = np.cos(18*np.pi*x1)
x2 = np.linspace(0, 2, 1000)
y2 = np.cos(18*np.pi*x2)

plt.plot(x1, y1, x2, y2)
plt.show()

"""We observe that x1 does not contain enough points
to create a correct plot of y1. x2 and y2 is correct"""
