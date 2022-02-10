import numpy as np
import matplotlib.pyplot as plt

def ForwardEuler(f, U0, T, N):
    """Solve u’=f(u,t), u(0)=U0, with n steps until t=T."""
    t = np.zeros(N+1)
    u = np.zeros(N+1) # u[n] is the solution at time t[n]
    u[0] = U0
    t[0] = 0
    dt = T/N
    for n in range(N):
        t[n+1] = t[n] + dt
        u[n+1] = u[n] + dt*f(u[n], t[n])
    return u, t

# u' = u/5, u0 = 0.1, t=[0, 20]
U0 = 0.1
f = lambda u, t: u/5

# (d)
u, t = ForwardEuler(f, U0, 20, 20//5)
plt.plot(t, u, label='dt=5')
plt.plot(t, 0.1*np.exp(0.2*t), '-', label='exact')
plt.legend()
plt.show()

# (e)
plt.clf()

for N in range(4, 10, 2):
    u, t = ForwardEuler(f, U0, 20, N)
    plt.plot(t, u, label=f'N={N}')

plt.plot(t, 0.1*np.exp(0.2*t), '-', label='exact')
plt.legend()
plt.show()

"""
Terminal> python simple_ODE_func.py.py
Observerer at tilnærming blir bedre med lavere dt-verdi dsv høyere N.
"""