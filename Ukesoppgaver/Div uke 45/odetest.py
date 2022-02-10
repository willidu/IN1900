from ODESolver import *
import numpy as np
import matplotlib.pyplot as plt

# Eksempel 1
def f(u, t):
    return 0.5*np.sqrt(u)*(1-(u/100))
metode = ForwardEuler(f)
metode.set_initial_condition(U0=0.01)
tp = np.linspace(0, 200, 400)
u, t = metode.solve(tp)
plt.plot(t, u)
plt.show()

# Eksempel 2
f = lambda u, t: np.sin(u) + np.log(abs(u)+1)
metode = RungeKutta4(f)
metode.set_initial_condition(0.5)
tp = np.linspace(0, 10, 500)
u, t = metode.solve(tp)
plt.plot(t, u)
plt.show()