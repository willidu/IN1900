m_e = 9.1064e-31  # kg
e = 1.6022e-19  # C
epsilon = 8.8542e-12  # C^2*s^2/kg/m^3
h = 6.66261e-34  # J*s

for n in range(1, 21):
    En = (-1) * ((m_e * (e ** 4)) / (8 * (epsilon ** 2) * (h ** 2))) \
         * (1 / (n ** 2))
    # print(f"{En:.2e} J")

for row in range(1, 6):
    for col in range(1, 6):
        print(row * col, end="\t")
    print()

i = 1
f = 1


def dE(i, f):
    dE = (-1) * ((m_e * (e ** 4)) / (8 * (epsilon ** 2) * (h ** 2))) \
         * ((1 / (i ** 2)) - (1 / (f ** 2)))
    return dE(i, f)


constant: float = float((-1) * ((m_e * (e ** 4)) / (8 * (epsilon ** 2) * (h ** 2))))

for m in range(1, 6):
    for n in range(1, 6):
        p = 1 / (m ** 2) - (1 / (n ** 2))
        print("%.3e", end="\t" % float(constant * p))
        # print(constant * p, end=" ")
    print()

"""
for i in range(1, n+1):
    for f in range(1, n+1):
        print(i * f, end="\t")
    print()

while f <= 5:
    print(dE(i, f))
    f += 1
    while i <= 5:
        i += 1
    else:
        break
        
"""
"""
f = 1
for i in range(1, 6):
    print(i, end=" ")
    while f <= 5:
        dE = (-1) * ((m_e * (e ** 4)) / (8 * (epsilon ** 2) * (h ** 2))) \
             * ((1 / (i ** 2)) - (1 / (f ** 2)))
        print("%g" % dE)
        f += 1
print(" ")
"""
"""
rad - i 1 - 5
kolonne f 1 - 5
"""

"""
f = 1
i = 1
while i and f <= 5:
    dE = (-1) * ((m_e * (e ** 4)) / (8 * (epsilon ** 2) * (h ** 2))) \
     * ((1 / (i ** 2)) - (1 / (f ** 2)))
    print(f"{i} \n{dE:.3e}")
    f += 1
"""
