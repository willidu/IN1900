
def sin_Taylor(x, n):
    j = n+1
    a = [x] * (n+1)
    s = [0] * (n+1)
    for j in range(1, j):
        a[j] = (-1 * ((x**2)/((2*j+1) * 2*j)) * a[j-1])
        s[j] += a[j]
        print(s[j], a[j])
    return s[-1], abs(a[-1])  # s_n+1 og a_n+1

print(sin_Taylor(0.001, 30))
