import matplotlib.pyplot as plt
import numpy as np
from ODESolver import *

def SEIR(u,t):
    beta = 0.4; r_ia = 0.1; r_e2=1.25;
    lmbda_1=0.33; lmbda_2=0.5; p_a=0.4; mu=0.2;

    S, E1, E2, I, Ia, R = u
    N = sum(u)
    dS  = -beta*S*I/N - r_ia*beta*S*Ia/N - r_e2*beta*S*E2/N
    dE1 = beta*S*I/N + r_ia*beta*S*Ia/N + r_e2*beta*S*E2/N - lmbda_1*E1
    dE2 = lmbda_1*(1-p_a)*E1 - lmbda_2*E2
    dI  = lmbda_2*E2 - mu*I
    dIa = lmbda_1*p_a*E1 - mu*Ia
    dR  = mu*(I + Ia)
    return [dS, dE1, dE2, dI, dIa, dR]

def test_SEIR():
    t = 0
    u = [1, 1, 1, 1, 1, 1]
    result = SEIR(u, t)
    expected = [-0.156666666666, -0.1733333333333, -0.302, 0.3, -0.068, 0.4]
    tol = 1e-10
    for a, b, in zip(result, expected):
        assert abs(a-b)<tol, 'Test failed'

def solve_SEIR(T, dt, S_0, E2_0):
    U = [S_0, 0, E2_0, 0, 0, 0]
    f = lambda u, t: u/6
    ForwardEuler(f)
    solver = ForwardEuler(SEIR)
    solver.set_initial_condition(U)
    t_val = np.linspace(0, T, round(T/dt+1))
    u, t = solver.solve(t_val)
    return u, t

def plot_SEIR(u, t):
    S = u[:,0]
    I = u[:,3]
    Ia = u[:,4]
    R = u[:,5]

    plt.plot(t, S, label='S')
    plt.plot(t, I, label='I')
    plt.plot(t, Ia, label='Ia')
    plt.plot(t, R, label='R')

    plt.xlim(0, max(t))
    plt.xlabel('Time [days]')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == '__main__':
    test_SEIR()

    u, t = solve_SEIR(150, 1.0, 5e6, 100)
    plot_SEIR(u, t)

"""
Terminal> python seir_func.py
Testfunksjon passerer og plot ser riktig ut.
"""