"""
Terminal> python approx_derivative_sine.py > data.txt
"""

import matplotlib.pyplot as plt
import numpy as np

def readfile(filename):
    with open(filename, 'r') as file:
        delta_x = []
        abs_error = []
        n = []

        for linecount, line in enumerate(file, start=1):
            if linecount % 2 == 0:
                data = line.split(',')
                delta_x.append(float(data[0][9:]))
                abs_error.append(float(data[3][12:]))
                n.append(int(''.join(letter for letter in data[-1] if letter.isdigit())))
    return np.array(delta_x), np.array(abs_error), np.array(n)

delta_x, abs_error, n = readfile('data.txt')

fig, ax = plt.subplots()

ax.plot(n, delta_x, '-',  label=r'$\Delta$ x')
ax.plot(n, abs_error, 'o-', label='Abs error')
ax.set_xlabel('n')
ax.set_ylabel(r'$log_{10}$')
ax.set_yscale('log')
ax.set_xlim(min(n), max(n))
ax.grid()
ax.legend()

# plt.show()
