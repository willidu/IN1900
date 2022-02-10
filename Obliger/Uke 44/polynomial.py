class Quadratic:
    def __init__(self, coefflist):
        self.c0 = coefflist[0]
        self.c1 = coefflist[1]
        self.c2 = coefflist[2]

    def __call__(self, x):
        return self.c0*x**2 + self.c1*x + self.c2

    def __str__(self):
        return f'{self.c0}*x**2 + {self.c1}*x + {self.c2}'

class Cubic(Quadratic):
    def __init__(self, coefflist):
        Quadratic.__init__(self, coefflist[1:])
        self.c3 = coefflist[0]
        self.coefflist = coefflist

    def __str__(self):
        return f'{self.c3}*x**3 + ' + Quadratic.__str__(self)

    def __call__(self, x):
        return self.c3*x**3 + self.c0*x**2 + self.c1*x + self.c2

    def derivative(self):
        coeff_prime = [3*self.c3, 2*self.c0, self.c1]
        return Quadratic(coeff_prime)

poly = Quadratic([1, 3, 2])
print(poly)
print(poly(1))
print(poly(2))

cub = Cubic([1, 3, 2, 4])
print(cub)
print(cub(1))
print(cub(2))
print(cub.derivative())

"""
Terminal> python polynomial.py
1*x**2 + 3*x + 2
6
12
1*x**3 + 3*x**2 + 2*x + 4        
10
28
3*x**2 + 6*x + 2
"""
