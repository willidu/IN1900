from ODESolver import *
import numpy as np
import matplotlib.pyplot as plt

# u' = u/5, u0 = 0.1, t=[0, 20]
U0 = 0.1
f = lambda u, t: u/5
method = ForwardEuler(f)
method.set_initial_condition(U0)

for dt in range(5, 0, -2):
    tp = np.linspace(0, 20, 20//dt)
    u, t = method.solve(tp)
    plt.plot(t, u, label=f'dt={dt}')

t_plot = np.linspace(0, 20, 1000)
plt.plot(t_plot, 0.1*np.exp(0.2*t_plot), '-', label='exact')
plt.legend()
plt.show()

"""
Terminal> python simple_ODE_class_ODESolver.py
"""