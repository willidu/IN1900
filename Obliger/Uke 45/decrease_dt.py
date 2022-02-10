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

n = (20, 30, 35, 40, 50, 100, 1000, 10000)

# x' = cos(6t)/(1+t+x), x0=0, t=[0, 10]
# x = u
f = lambda u, t: np.cos(6*t)/(1+t+u)
for N in n:
    method = ForwardEuler_v1(f, 0, 10, N-1)
    u, t = method.solve()
    plt.plot(t, u, label=f'N={N}')
plt.legend()
plt.show()

"""
Terminal> python decrease_dt.py
"""