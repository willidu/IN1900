from Parabola import Parabola

class F(Parabola):
    def __init__(self, A, w, a, b, c):
        Parabola.__init__(self, a, b, c)
        self.A = A
        self.w = w
        self.p = Parabola(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        from math import sin
        return self.A*sin(self.w * x) + self.p(x)

    def __str__(self):
        return f'{self.A}*sin({self.w}x) ' + self.p.__str__()

test = F(1, 0.5, 0, 3, 1)
print(test)
print(test.table(0, 10, 11))