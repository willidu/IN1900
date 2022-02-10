import numpy as np
import matplotlib.pyplot as plt

with open('xy.dat', 'r') as file:
    x = []
    y = []
    for line in file:
        values = line.split()
        x.append(float(values[0]))
        y.append(float(values[1]))

y = np.array(y)
print(f"Mean y = {np.mean(y)}, max = {max(y)}, min = {min(y)}")

plt.plot(x, y)
plt.show()
