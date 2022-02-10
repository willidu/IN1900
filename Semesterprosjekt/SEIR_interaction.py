from SEIR import *
import numpy as np

class RegionInteraction(Region):
    def __init__(self, name, S_0, E2_0, lat, long):
        super().__init__(name, S_0, E2_0)
        self.lat = lat*np.pi/180; self.long = long*np.pi/180

    def distance(self, other):
        term = np.sin(self.lat)*np.sin(other.lat) + np.cos(self.lat)*np.cos(other.lat)*np.cos(abs(self.long-other.long))
        if 1-term >= 0:
            dSigma_ij = np.arccos(term)
        else:
            print(f'arccos({term}) not defined. Rounding to arccos(1)')
            dSigma_ij = np.arccos(1)
        return 6400 * dSigma_ij

class ProblemInteraction(ProblemSEIR):
    def __init__(self, region, area_name, beta, r_ia = 0.1, r_e2=1.25, lmbda_1=0.33, lmbda_2=0.5, p_a=0.4, mu=0.2, k=0.01):
        super().__init__(region, beta, r_ia = 0.1, r_e2=1.25, lmbda_1=0.33, lmbda_2=0.5, p_a=0.4, mu=0.2)
        self.area_name = area_name; self.k = k

    def get_population(self):
        s = 0
        for regions in self.region:
            s += regions.population
        return s

    def set_initial_condition(self):
        self.initial_condition = []
        for regions in self.region:
            self.initial_condition += regions.U
        return self.initial_condition

    def __call__(self, u, t):
        beta = self.beta(t); r_ia = self.r_ia; r_e2 = self.r_e2
        lmbda_1 = self.lmbda_1; lmbda_2 = self.lmbda_2; p_a = self.p_a
        mu = self.mu; n = len(self.region)
        
        SEIR_list = [u[i:i+6] for i in range(0, len(u), 6)]
        E2_list = [u[i] for i in range(2, len(u), 6)]
        Ia_list = [u[i] for i in range(3, len(u), 6)]

        derivative = []
        for i in range(n):
            N = self.region[i].population
            S, E1, E2, I, Ia, R = SEIR_list[i]
            dS = -beta*S*I/N 
            for j in range(n):
                #if i == j:
                    #continue
                E2_other = E2_list[j]
                Ia_other = Ia_list[j]
                N_other = self.region[j].population
                d_ij = self.region[i].distance(self.region[j])
                
                dS  += -r_ia*beta*S*(Ia_other/N_other*np.exp(-self.k*d_ij)) - r_e2*beta*S*(E2_other/N_other*np.exp(-self.k*d_ij))
            dE1 = -dS - lmbda_1*E1
            dE2 = lmbda_1*(1-p_a)*E1 - lmbda_2*E2
            dI  = lmbda_2*E2 - mu*I
            dIa = lmbda_1*p_a*E1 - mu*Ia
            dR  = mu*(I + Ia)
            derivative += [dS, dE1, dE2, dI, dIa, dR]
        return derivative

    def split_solution(self, u, t):
        self.t = t
        n = len(t)
        n_reg = len(self.region)
        
        self.S = np.zeros(n); self.E1 = np.zeros(n); self.E2 = np.zeros(n)
        self.I = np.zeros(n); self.Ia = np.zeros(n); self.R = np.zeros(n)

        SEIR_list = [u[:, i:i+6] for i in range(0, n_reg*6, 6)]
        for part, SEIR in zip(self.region, SEIR_list):
            part.set_SEIR_values(SEIR, t)
            self.S += part.S; self.E1 += part.E1; self.E2 += part.E2
            self.I += part.I; self.Ia += part.Ia; self.R += part.R
        return

    def plot(self):
        plt.plot(self.t, self.S, label='Susceptible')
        plt.plot(self.t, self.I, label='Infected')
        plt.plot(self.t, self.Ia, label='Asymptomatic')
        plt.plot(self.t, self.R, label='Recovery')

        plt.xlim(0, max(self.t))
        plt.xlabel('Time [days]')
        plt.ylabel('Population')
        plt.title(self.area_name, fontsize=11)
        plt.grid()
        return

if __name__ == '__main__':
    innlandet = RegionInteraction('Innlandet',S_0=371385,E2_0=0, lat=60.7945, long=11.0680)
    oslo = RegionInteraction('Oslo',S_0=693494,E2_0=100, lat=59.9,long=10.8)
    print(oslo.distance(innlandet))
 
    problem = ProblemInteraction([oslo,innlandet],'Norway_east', beta=0.4)
    print(problem.get_population())
    problem.set_initial_condition()
    print(problem.initial_condition)
    u = problem.initial_condition
    print(problem(u,0))

    solver = SolverSEIR(problem,T=150,dt=1.0)
    solver.solve()
    problem.plot()
    plt.legend()
    plt.show()

    """
    Terminal> python SEIR_interaction.py
    101.00809386280783
    1064979
    [693494, 0, 100, 0, 0, 0, 371385, 0, 0, 0, 0, 0]
    [-49.99279117178061, 49.99279117178061, -50.0, 50.0, 0.0, 0.0, -9.750265859422228, 9.750265859422228, 0.0, 0.0, 0.0, 0.0]
    Observerer at startverdi for self.S er riktig
    Plottet set korrekt ut.
    """