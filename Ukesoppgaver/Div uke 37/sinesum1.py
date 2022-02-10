import math


def S(t, n, T=2 * math.pi):
    sum = 0
    for i in range(n + 1):
        sum += 4 / math.pi * (1 / (2 * i - 1)) * math.sin((2 * (2 * i - 1) * math.pi * t) / T)
    return sum


def f(t, T=2 * math.pi):
    if 0 < t < T / 2:
        return 1
    elif t == T / 2:
        return 0
    elif T / 2 < t < T:
        return -1
    else:
        return "wtf"


T = 2 * math.pi
n = [1, 3, 5, 10, 30, 100]
t = [0.01 * T, 0.25 * T, 0.49 * T]

nest = []
for i in range(len(n)):
    nest.append([n[i], [t[r] for r in range(len(t))]])

r = 0
i = 0
for i in range(len(t)):
    for r in range(len(n)):
        print(f"t = {t[i]:5.3f} n = {n[r]}, error = {f(t[i]) - S(t[i], n[r]):5.4f}")
