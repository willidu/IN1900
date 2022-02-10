def sumint(n):
    i = 1
    s = 0
    while i <= n:
        s += i
        i += 1
    return s


print(sumint(5))


def sumb(n):
    s = n * (n + 1) / 2
    return s


print(int(sumb(5)))
