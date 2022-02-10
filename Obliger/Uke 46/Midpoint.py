from ODESolver import *
import numpy as np
import matplotlib.pyplot as plt

class Midpoint(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = t[n+1] - t[n]
        k1 = f(u[n], t[n])
        k2 = f(u[n] + (dt/2)*k1, t[n] + dt/2)
        unew = u[n] + dt*k2
        return unew

f = lambda u, t: np.cos(t) - t * np.sin(t)
U0 = 0
tp = np.linspace(0, 4*np.pi, 20)
plt.plot(tp, tp*np.cos(tp), 'k', label='Analytical solution')

for solver in (Midpoint, ForwardEuler):
    method = solver(f)
    method.set_initial_condition(U0)
    u, t = method.solve(tp)
    plt.plot(t, u, '--', label=solver.__name__)

plt.legend()
plt.show()

"""
Terminal> python Midpoint.py
"""