import numpy as np
"""
t = 15
condlist = [t<10, (t>10)&(t<20), t>20]
funclist = [0, lambda t: t**2, 13]

y = np.piecewise(t, condlist, funclist)
print(t, condlist, funclist)
print(y)
"""
x = np.asarray([5, 6, 10])
condlist = [x<=5, (x>5)&(x<=6), x>6]
print(condlist)
funclist = [lambda x: 0.4, lambda x: 0.0625, lambda x: 0.0875]
y = np.piecewise(x, condlist, funclist)
print(y)
v = np.piecewise(x, [x<=5, (x>5)&(x<=6), x>6], [lambda x: 0.4, lambda x: 0.0625, lambda x: 0.0875])
print(v)

from covid19 import Beta
h = Beta('time_R_table.txt', 5)
h.get_R_values()
h.get_conditions()
h.get_beta_values()
# print(b.get_conditions())
# print(b.get_beta_values())

h.plot()