import numpy as np

x = [3.14]
for n in range(1, 3):
    x.append(x[n-1] - (np.sin(x[n-1]))/np.cos(x[n-1]))

print(f"np.pi = {np.pi:.13f} \nx0 = {x[0]} \nx1 = {x[1]:.13f} \nx2 = {x[2]:.13f}")

"""
Terminal> python finding_pi.py
np.pi = 3.1415926535898 
x0 = 3.14 
x1 = 3.1415926549364 
x2 = 3.1415926535898
"""