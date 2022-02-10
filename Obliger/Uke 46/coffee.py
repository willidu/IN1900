from ODESolver import *
import numpy as np
import matplotlib.pyplot as plt

class Cooling:
    def __init__(self, h, Ts):
        self.h = h
        self.Ts = Ts

    def __call__(self, T, t):
        return -self.h*(T-self.Ts)

def estimate_h(t1, Ts, T0, T1):
    h = (T1 - T0)/(t1*(Ts - T0))
    return h

def test_Cooling():
    h = estimate_h(5, 20, 100, 95)
    c = Cooling(h, 20)
    calculated = c(100, 5)
    expected = (100-95)/(-5)
    assert abs(expected-calculated)<1e-8, 'Test failed'

test_Cooling()

for Ts in (20, 25):
    h = estimate_h(15, Ts, 95, 92)
    c = Cooling(h, Ts)
    method = ForwardEuler(c)
    method.set_initial_condition(95)
    tp = np.linspace(0, 1200, 1201)
    u, t = method.solve(tp)
    plt.plot(t, u, label=f'Ts = {Ts}')

plt.legend()
plt.xlim(0, 1200)
plt.ylim(20, 100)
plt.grid()
plt.show()

"""
Terminal> python coffee.py
Testfuksjon passerer.
"""