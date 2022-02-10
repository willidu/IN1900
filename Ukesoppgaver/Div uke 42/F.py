class F:
    def __init__(self, a, w):
        self.a = a
        self.w = w

    def value(self, x):
        from math import exp, sin
        return exp(-self.a*x)*sin(self.w*x)


"""
>>> from F import F
>>> from math import pi
>>> f = F(1.0, 0.1)
>>> print(f.value(pi))
0.01335383513703555
>>> f.a = 2 
>>> print(f.value(pi))
0.0005770715401197441
"""