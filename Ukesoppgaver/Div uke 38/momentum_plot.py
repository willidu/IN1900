import numpy as np
import matplotlib.pyplot as plt

m = 5
c = 3e8

n = 100
v = np.linspace(0, 0.9*c, n+1)

p_clas = m * v
gamma = 1 / (np.sqrt(1 - (v**2/c**2)))
p_rel = m * v * gamma

plt.plot(v, p_clas, v, p_rel)
plt.xlim(0, 0.9*c)
plt.xlabel("$10^8$ m/s")
plt.ylabel("Momentum")
plt.legend(["$p_c$", "$p_r$"])
plt.show()
