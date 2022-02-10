import numpy as np
import matplotlib.pyplot as plt

# Task (a) and (c):
def heuns_method(f, U0, T, N):
    t = np.zeros(N+1)
    u = np.zeros(N+1)
    u[0] = U0
    t[0] = 0
    dt = T/N
    for n in range(N):
        k1 = f(u[n], t[n])
        k2 = f(u[n] + dt*k1, t[n] + dt)
        t[n+1] = t[n] + dt
        u[n+1] = u[n] + dt*(k1/2 + k2/2)
    return u, t

# u' = u/5, u0 = 0.1, t=[0, 20]
U0 = 0.1
f = lambda u, t: u/5

n = (1, 2, 5, 10)
for N in n:
    u, t = heuns_method(f, U0, 10, N)
    plt.plot(t, u, label=f'N={N}')
plt.plot(t, 0.1*np.exp(0.2*t), '-', label='exact')
plt.legend()
plt.show()

"""
Terminal> python heuns_method_func.py
Observerer numerisk løsning nærmer seg analytisk med flere punkter.
"""