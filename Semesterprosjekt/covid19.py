from SEIR_interaction import *
from datetime import date

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
print(reg)

"""
Terminal> python covid19.py
[<SEIR_interaction.RegionInteraction object at 0x000002699C08C550>, 
... 
<SEIR_interaction.RegionInteraction object at 0x00000269ABF93490>]
"""

def covid19_Norway(beta, filename, num_days, dt):
    region_list = read_regions(filename)
    problem = ProblemInteraction(region_list, 'Norway', beta)
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

covid19_Norway(0.4, 'fylker.txt', 150, 1.0)

"""
Terminal> python covid19.py
Plot ser riktig ut. Observerer at peak gul linje i siste plot er på rundt 174 000
personer. 0.05*174000 = 8700 >> 700.
"""

def get_R_values(filename):
    """ Reads table from FHI and saves intervals with time and R values. """
    with open(filename, 'r') as file:
        file.readline()
        L1 = file.readline().split()

        I0_ = L1[0].split('.')
        I0 = date(int(I0_[-1]), int(I0_[-2]), int(I0_[-3]))

        r = [float(L1[-1])]
        t = [0]

        dD = 0
        for lines in file:
            line = lines.split()
            D_ = line[0].split('.')
            D = date(int(D_[-1]), int(D_[-2]), int(D_[-3]))
            dD = (D-I0).days
            r.append(float(line[-1]))
            t.append(dD)
    return t, r

def R(tp, t, r):
    """ Returns correct R value for corresponding time interval. """
    for i in range(1, len(r)):
        if t[i-1] <= tp < t[i]:
            return r[i-1]
        elif tp >= max(t):
            return r[-1]
        
def R_to_beta(R_, r_ia = 0.1, r_e2=1.25, lmbda_2=0.5, mu=0.2):
    """ Rearange formula given in task and solve for Beta. """
    constant = lmbda_2*mu/(r_e2*mu + lmbda_2*r_ia + lmbda_2)
    return R_*constant

t, r = get_R_values('time_R_table.txt')

def beta(tp):
    R_ = R(tp, t, r)
    b = R_to_beta(R_)
    return b

num_days = int((date.today() - date(2020, 2, 15)).days)

def plot_beta(num_days, beta, R, t, r):
    t_array = np.linspace(0, num_days, num_days+1)
    r_array = np.zeros(num_days+1)
    beta_array = np.zeros(num_days+1)

    for i in range(num_days+1):
        beta_array[i] = beta(t_array[i])
        r_array[i] = R(t_array[i], t, r)

    plt.clf()
    plt.plot(t_array, beta_array, label=r'$\beta$')
    plt.plot(t_array, r_array, label='R')
    plt.xlim(0, max(t_array))
    plt.title(r'$\beta$ model')
    plt.xlabel('Time [days]')
    plt.legend()
    plt.grid()
    plt.show()
plot_beta(num_days, beta, R, t, r)

"""
Terminal> python covid19.py
Beta verider ser ut til å samsvare greit med R verdier fra tabell.
"""

covid19_Norway(beta, 'fylker.txt', num_days, 1.0)

"""
Terminal> python covid19.py
Koden funker men usikker på om plottet stemmer. 
"""