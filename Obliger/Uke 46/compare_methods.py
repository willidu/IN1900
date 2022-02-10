from ODESolver import*
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

class Heun(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = t[n+1] - t[n]
        k1 = f(u[n], t[n])
        k2 = f(u[n] + dt*k1, t[n] + dt)
        unew = u[n] + dt*(k1/2 + k2/2)
        return unew

f = lambda u, t: t*np.cos(t) - np.sin(t); U0 = 2
y = lambda t: t*np.sin(t) + 2*np.cos(t)

fig, ax = plt.subplots(nrows=1, ncols=3)

for i, solver in enumerate((Midpoint, Heun, RungeKutta4), 0):
    
    for N in (20, 25, 50, 150):
        tp = np.linspace(0, 8*np.pi, N)
        method = solver(f)
        method.set_initial_condition(U0)
        u, t = method.solve(tp)
        ax[i].plot(t, u, label=f'N={N}')
    
    ax[i].plot(tp, y(tp), 'k--', label='Analytical (N=150)')
    ax[i].set_title(solver.__name__)
    ax[i].set_xlim(0, 8*np.pi)
    ax[i].legend()
    ax[i].grid()
    
plt.show()

"""
Terminal> python compare_methods.py
"""