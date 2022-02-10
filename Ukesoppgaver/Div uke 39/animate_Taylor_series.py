import numpy as np


def animate_series(fk, M, N, xmin, xmax, ymin, ymax, n, exact):
    import numpy as np
    import matplotlib.pyplot as plt
    import math

    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
    plt.xlabel("x")
    plt.ylabel("(S(x;M;N)")
    labels = [f"{str(exact.__name__)}(x)", f"Taylor approximation: n = {n}"]

    x = np.linspace(xmin, xmax, n)
    s = np.zeros(n)
    k = M  # Initial k value is M
    f = eval(fk)  # Evaluating expression fk with k=M and x array
    lines = plt.plot(x, f)  # plot first approximation
    for k in range(M, N + 1):
        s = s + eval(fk)
        lines[0].set_ydata(s)
        labels[1] = f"Taylor approximation: k = {k}"
        plt.plot(x, exact(x), "g")
        plt.legend(labels, loc='upper right')
        plt.pause(0.2)
        plt.draw()
    plt.pause(1)
    plt.clf()
    plt.cla()
    return

animate_series('((-1)**k * x**(2*k+1)) / (math.factorial(2*k+1))', 0, 40, 0, 13 * np.pi, -2, 2, 1000, np.sin)

def h(x):
    return np.exp(-x)
# funker også med h(x) = lambda x: np.exp(-x)
# og samme måte for å definere fk, egentlig lettere enn eval metoden
animate_series('((-x)**k)/(math.factorial(k))', 0, 30, 0, 15, -0.5, 1.4, 1000, h)
