import numpy as np
import matplotlib.pyplot as plt

class ForwardEuler_v1:
    def __init__(self, f, U0, T, N):
        self.f, self.U0, self.T, self.N = f, U0, T, N
        self.dt = T/N
        self.u = np.zeros(self.N+1)
        self.t = np.zeros(self.N+1)
    def solve(self):
        """Compute solution for 0 <= t <= T."""
        self.u[0] = float(self.U0)
        for n in range(self.N):
            self.n = n
            self.t[n+1] = self.t[n] + self.dt
            self.u[n+1] = self.advance()
        return self.u, self.t
    def advance(self):
        """Advance the solution one time step."""
        u, dt, f, n, t = self.u, self.dt, self.f, self.n, self.t
        unew = u[n] + dt*f(u[n], t[n])
        return unew

class F:
    def __init__(self, expr):
        self.f = lambda u, t: eval(expr)

    def __call__(self, u, t):
        return self.f(u, t)

# u' = u/5, u0 = 0.1, t=[0, 20]
U0 = 0.1
f = F('u/5')

for N in range(4, 10, 2):
    method = ForwardEuler_v1(f, U0, 20, N)
    u, t = method.solve()
    plt.plot(t, u, label=f'N={N}')

tp = np.linspace(0, 20, 1000)
plt.plot(tp, 0.1*np.exp(0.2*tp), '-', label='exact')
plt.legend()
plt.show()

"""
Terminal> python simple_ODE_class.py
Samme plot som i E.1.
"""