n = 10
v0 = 50
g = 9.81
t0 = 0
t_max = 2 * v0 / g
h = (t_max - t0) / n

t = [0] * (n + 1)
y = [0] * (n + 1)
for i in range(n + 1):
    t[i] = i * h
    y[i] = v0 * t[i] - 0.5 * g * t[i] ** 2
    print(f"{t[i]:10.3f}  {y[i]:10.3f}")
