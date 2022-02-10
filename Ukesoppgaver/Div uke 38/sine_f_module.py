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