import matplotlib.pyplot as plt
import numpy as np
from ODESolver import *

class Region:
    def __init__(self, name, S_0, E2_0):
        self.name = name; self.S_0 = S_0; self.E2_0 = E2_0
        self.E1_0 = 0; self.I_0 = 0; self.Ia_0 = 0; self.R_0 = 0

        self.U = [self.S_0, self.E1_0, self.E2_0, self.I_0, self.Ia_0, self.R_0]
        self.population = sum(self.U)

    def set_SEIR_values(self, u, t):
        self.S = u[:,0]; self.E1 = u[:,1]; self.E2 = u[:,2]
        self.I = u[:,3]; self.Ia = u[:,4]; self.R = u[:,5]
        self.t = t
        return ((self.S, self.E1, self.E2, self.I, self.Ia, self.R), self.t)

    def plot(self):
        t = self.t
        plt.plot(t, self.S, label='Susceptible')
        plt.plot(t, self.I, label='Infected')
        plt.plot(t, self.Ia, label='Asymptomatic')
        plt.plot(t, self.R, label='Recovery')

        plt.xlim(0, max(t))
        plt.xlabel('Time [days]')
        plt.ylabel('Population')
        plt.grid()
        return

class ProblemSEIR:
    def __init__(self, region, beta, r_ia = 0.1, r_e2=1.25, lmbda_1=0.33, lmbda_2=0.5, p_a=0.4, mu=0.2):

        if isinstance(beta, (float, int)):
            self.beta = lambda t: beta
        elif callable(beta):
            self.beta = beta
        
        self.region = region; self.r_ia = r_ia; self.r_e2 = r_e2; self.lmbda_1 = lmbda_1
        self.lmbda_2 = lmbda_2; self.p_a = p_a; self.mu = mu

    def set_initial_condition(self):
        self.initial_condition = [self.region.S_0, self.region.E1_0, self.region.E2_0, self.region.I_0, self.region.Ia_0, self.region.R_0]
        return self.initial_condition

    def get_population(self):
        return self.region.population

    def split_solution(self, u, t):
        ((self.S, self.E1, self.E2, self.I, self.Ia, self.R), self.t) = self.region.set_SEIR_values(u, t)
        return

    def __call__(self, u, t):
        beta = self.beta(t); r_ia = self.r_ia; r_e2 = self.r_e2; lmbda_1 = self.lmbda_1
        lmbda_2 = self.lmbda_2; p_a = self.p_a; mu = self.mu 
        (S, E1, E2, I, Ia, R) = u
        N = sum(u)

        dS  = -beta*S*I/N - r_ia*beta*S*Ia/N - r_e2*beta*S*E2/N
        dE1 = beta*S*I/N + r_ia*beta*S*Ia/N + r_e2*beta*S*E2/N - lmbda_1*E1
        dE2 = lmbda_1*(1-p_a)*E1 - lmbda_2*E2
        dI  = lmbda_2*E2 - mu*I
        dIa = lmbda_1*p_a*E1 - mu*Ia
        dR  = mu*(I + Ia)
        return [dS, dE1, dE2, dI, dIa, dR]

class SolverSEIR:
    def __init__(self, problem, T, dt):
        self.problem = problem; self.T = T; self.dt = dt
        self.total_population = problem.get_population()

    def solve(self, method=ForwardEuler):
        solver = method(self.problem)
        solver.set_initial_condition(self.problem.set_initial_condition())
        t = np.linspace(0, self.T, round(self.T/self.dt+1))
        u, t = solver.solve(t)
        self.problem.split_solution(u, t)
        return

if __name__ == '__main__':
    nor = Region('Norway',S_0=5e6,E2_0=100)
    print(nor.name, nor.population)
    S_0, E1_0, E2_0 = nor.S_0, nor.E1_0, nor.E2_0
    I_0, Ia_0, R_0 = nor.I_0, nor.Ia_0, nor.R_0
    print(f'S_0 = {S_0}, E1_0 = {E1_0}, E2_0 = {E2_0}')
    print(f'I_0 = {I_0}, Ia_0 = {Ia_0}, R_0 = {R_0}')
    u = np.zeros((2,6))
    u[0,:] = [S_0, E1_0, E2_0, I_0, Ia_0, R_0]
    nor.set_SEIR_values(u,0)
    print(nor.S, nor.E1, nor.E2, nor.I, nor.Ia, nor.R)
    
    """
    Terminal> python SEIR.py
    Norway 5000100.0
    S_0 = 5000000.0, E1_0 = 0, E2_0 = 100
    I_0 = 0, Ia_0 = 0, R_0 = 0
    [5000000.       0.] [0. 0.] [100.   0.] [0. 0.] [0. 0.] [0. 0.]
    """

    problem = ProblemSEIR(nor,beta=0.4)
    problem.set_initial_condition()
    print(problem.initial_condition)
    print(problem.get_population())
    print(problem([1,1,1,1,1,1],0))

    """
    Terminal> python SEIR.py
    [5000000.0, 0, 100, 0, 0, 0]
    5000100.0
    [-0.15666666666666668, -0.17333333333333334, -0.302, 0.3, -0.068, 0.4]
    """

    solver = SolverSEIR(problem,T=150,dt=1.0)
    solver.solve()
    nor.plot()
    plt.legend()
    plt.show()

    """
    Terminal> python SEIR.py
    Får opp et plot identisk med det i oppgave 1.
    """
