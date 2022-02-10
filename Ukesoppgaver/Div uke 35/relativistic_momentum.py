import math

c = 3e8  # m/s
m = 1200  # kg
v = 0  # c

while v <= 0.9:
    p = m * v * c
    gamma = 1 / (math.sqrt(1 - (((v * c) ** 2) / (c ** 2))))
    p_rel = m * v * c * gamma
    print(f"{v:.1f}c, {p:.4e}, {p_rel:.4e}")
    v += 0.1
