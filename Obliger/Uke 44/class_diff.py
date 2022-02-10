import numpy as np
import matplotlib.pyplot as plt

class Diff:
    def __init__(self, f, h=1e-5):
        self.f = f
        self.h = h

    def diff1(self, x):
        return (self.f(x + self.h) - self.f(x))/self.h
    
    def diff2(self, x):
        return (self.f(x + self.h) - self.f(x - self.h)) / (2 * self.h)

    def diff3(self, x):
        f = self.f
        h = self.h
        return (-1*f(x+2*h)+8*f(x+h)-8*f(x-h)+f(x-2*h))/(12*h)

def f(x):
    return np.sin(2*np.pi*x)

def f_prime(x):
    return 2*np.pi*np.cos(2*np.pi*x)

df = Diff(f)
x = np.linspace(-1, 1, 100)

#Plot 1
h = [0.9, 0.6, 0.3, 0.1]
for h in h:
    df.h = h
    # plt.plot(x, df.diff1(x), label=f'Diff1, h = {df.h}')
    # plt.plot(x, df.diff2(x), label=f'Diff2, h = {df.h}')
    plt.plot(x, df.diff3(x), label=f'Diff3, h = {df.h}')

plt.plot(x, f_prime(x), label='exact')
plt.xlim(-1, 1)
plt.legend(ncol = 3)
plt.grid()
plt.show()
