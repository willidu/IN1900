m_e = 9.1064e-31  # kg
e = 1.6022e-19  # C
epsilon = 8.8542e-12  # C^2*s^2/kg/m^3
h = 6.66261e-34  # J*s
constant = (-1) * ((m_e * (e ** 4)) / (8 * (epsilon ** 2) * (h ** 2)))

for i in range(1, 6):
    for f in range(1, 6):
        n = (1 / i ** 2) - (1 / f ** 2)
        print(n * constant, end="\t")
    print()
print("-----------------")

"""
for n in range(1, 21):
    En = (-1) * ((m_e * (e ** 4)) / (8 * (epsilon ** 2) * (h ** 2))) \
         * (1 / (n ** 2))
    # print(f"{En:.2e} J")
"""