from Line import Line

class Parabola(Line):
    def __init__(self, c0, c1, c2):
        Line.__init__(self, c0, c1) # let Line store c0 and c1
        self.c2 = c2
    
    def __call__(self, x):
        return Line.__call__(self, x) + self.c2*x**2

    def __str__(self):
        return f'{self.c2}x**2 + {self.c1}x + {self.c0}'