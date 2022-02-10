import numpy as np
import matplotlib.pyplot as plt


def arclength(f, a, b, n):
    """Takes f as a function f = lambda x: x**2"""
    import numpy as np

    x = np.linspace(a, b, n+1)

    # Prints f(x) values
    f_x = np.array(f(x))
    # print(f_x)

    # Prints f'(x) values
    h = 1e-12
    f_prime_x = (f(x+h) - f(x)) / h
    # print(f_prime_x)

    g = np.sqrt(1 + f_prime_x ** 2)

    s = np.zeros(n+1)
    for n in range(1, n+1):
        s[n] = s[n - 1] + 0.5 * (x[n] - x[n - 1])*(g[n-1] + g[n])
    return x, s

def f(x):
    return 1/(np.sqrt(2*np.pi))*np.exp(-4*x**2)

a_val = -2
b_val = 2
n_points = 100
arc = arclength(f, a=a_val, b=b_val, n=100)

x = np.linspace(a_val, b_val, n_points+1)

plt.plot(arc[0], arc[1], label="s(x)")
plt.plot(x, f(x))
plt.show()
