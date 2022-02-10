R = 8.314  # J/K/mol
T = 273  # K
p = 1e5  # Pa
V = 4e-3  # m^-3

n = (p * V) / (R * T)
print(f"a) n = {n:.3f} mol")

m = 11.45 - 4.376  # g
M = m / n
print(f"b) Molar mass = {M:.3f} g/mol")
