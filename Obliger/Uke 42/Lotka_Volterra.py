import matplotlib.pyplot as plt

a = 0.04
b = 0.1
c = 0.005
e = 0.2

R = [100]
F = [20]

for n in range(1, 500):
    R.append(R[n-1] + a*R[n-1] - c*R[n-1]*F[n-1])
    F.append(F[n-1] + e*c*R[n-1]*F[n-1] - b*F[n-1])

x = range(0, 500)
plt.plot(x, R, label='Rabbits')
plt.plot(x, F, label='Foxes')
plt.xlabel('Time [weeks]')
plt.ylabel('Number of animals in pop.')
plt.xlim(0, 500)
plt.legend()
plt.grid()
plt.show()

"""
Terminal> python Lokta_Volterra.py

Printer graf som forventet.
"""