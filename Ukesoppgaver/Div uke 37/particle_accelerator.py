# m = 9.1e-31  # kg
# q = -1.6e-19  # C
E = 0.02  # N/C

v0 = input("Initial velocity (v0) = ? \n")
t = input("Time (t) = ? \n")
m = input("Mass (m) = ? \n")
q = input("Electric charge (q) = ? \n")
try:
    m = float(m)
    v0 = float(v0)
    t = float(t)
    q = float(q)
except ValueError:
    print("Input must be a number, stopping program")
    exit()
else:
    m = float(m)
    v0 = float(v0)
    t = float(t)
    q = float(q)


def x(t):
    dist = v0 * t + 0.5 * ((q * E) / m) * t ** 2
    return dist


def v(t):
    vel = v0 + ((q * E) / m) * t ** 2
    return vel


print(f"x({t}) = {x(t):.3e}, v({t}) = {v(t):.3e}")