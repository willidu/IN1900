import numpy as np
import matplotlib.pyplot as plt
from datetime import date
from SEIR_interaction import *

class Beta(ProblemInteraction):
    def __init__(self, region, area_name, table_filename, r_ia = 0.1, r_e2=1.25, lmbda_1=0.33, lmbda_2=0.5, p_a=0.4, mu=0.2, k=0.01):
        self.r_ia = r_ia; self.r_e2 = r_e2
        self.lmbda_2 = lmbda_2; self.mu = mu

        self.filename = table_filename

        self.get_R_values()

        super().__init__(region, area_name, beta, r_ia = 0.1, r_e2=1.25, lmbda_1=0.33, lmbda_2=0.5, p_a=0.4, mu=0.2, k=0.01)

    def get_R_values(self):
        """ Reads table from FHI and saves intervals with time and R values. """
        with open(self.filename, 'r') as file:
            file.readline()
            L1 = file.readline().split()

            I0_ = L1[0].split('.')
            I0 = date(int(I0_[-1]), int(I0_[-2]), int(I0_[-3]))

            self.r = [float(L1[-1])]
            self.t = [0]

            dD = 0
            for lines in file:
                line = lines.split()
                D_ = line[0].split('.')
                D = date(int(D_[-1]), int(D_[-2]), int(D_[-3]))
                dD = (D-I0).days
                self.r.append(float(line[-1]))
                self.t.append(dD)
        return self.t, self.r

    def beta(self, tp):
        t = self.t; r = self.r
        
        for i in range(1, len(r)):
            if t[i-1] <= tp < t[i]:
                R = r[i-1]
            elif tp >= max(t):
                R = r[-1]

        constant = self.lmbda_2*self.mu/(self.r_e2*self.mu + self.lmbda_2*self.r_ia + self.lmbda_2)
        return R * constant

    def __call__(self, tp):
        return self.beta(tp)

    """
    def get_conditions(self):
        self.dT = np.linspace(0, self.T, self.T+1)
        
        self.funclist = np.zeros(len(self.dT))
        for i in range(len(self.dT)):
            self.funclist[i] = self.returnbeta(self.dT[i])
        
        self.condlist = []
        for i in range(1, len(self.t)):
            self.condlist.append(np.logical_and(self.dT>=self.t[i-1], self.dT<self.t[i]))
        self.condlist.append(self.dT>=self.t[-1])
        return self.condlist, self.funclist
    
    def get_beta_values(self):
        # Returns array with Beta values, same dimension as self.dT
        return np.piecewise(self.dT, self.condlist, self.funclist)

    def plot_beta(self):
        plt.clf()
        #plt.plot(self.dT, self.get_beta_values(), label=r'$\beta$')
        plt.plot(self.dT, self.returnbeta(self.dT), label='test')
        plt.xlim(0, self.T)
        plt.xlabel('Time [days]')
        plt.legend()
        plt.title(r'$\bf \beta\ model$', fontsize=18)
        plt.grid()
    """
    def skrivut(self):
        # Prints time and R values (as intervals)
        for a, b in zip(self.t, self.r):
            print(a, b)
        return

def read_regions(filename):
    regions = []
    with open(filename, 'r') as file:
        for lines in file:
            line = lines.split(';')[1:]

            name = line[0].strip().replace('Ã¸', 'ø')
            S_0 = float(line[1])
            E1_0 = float(line[2])
            lat = float(line[3])
            long = float(line[4])

            reg = RegionInteraction(name, S_0, E1_0, lat, long)
            regions += [reg]
    return regions

reg = read_regions('fylker.txt')

def covid19_Norway2(region_filename, R_filename, num_days, dt):
    region_list = read_regions(region_filename)
    problem = Beta(region_list, 'Norway', R_filename)
    solver = SolverSEIR(problem, num_days, dt)
    solver.solve()

    fig = plt.figure(figsize=(12, 10))
    index = 1
    for region in region_list:
        plt.subplot(4, 3, index)
        plt.gca().set_title(region.name, fontsize=11)
        region.plot()
        plt.gca().set_ylabel('')
        plt.gca().set_xlabel('')
        index += 1
    
    plt.subplot(4,3, index)
    plt.subplots_adjust(hspace = 0.65, wspace=0.5, top=0.85)
    problem.plot()
    plt.gca().set_ylabel('')
    plt.gca().set_xlabel('')

    plt.subplot(4, 3, 2)
    plt.legend(loc='upper center', ncol=4, bbox_to_anchor=(0.5, 1.7))
    fig.suptitle(f'Covid-19 spread in {problem.area_name} over {num_days:.0f} days', fontsize=16)
    fig.supxlabel('Time [days]')
    fig.supylabel('Population')
    plt.show()

num_days = int((date.today() - date(2020, 2, 15)).days)
covid19_Norway2('fylker.txt', 'time_R_table.txt', num_days, 1.0)