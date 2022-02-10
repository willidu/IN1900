from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

class RightTriangle:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        if a < 0 or b < 0:
            raise ValueError
        else:
            self.c = sqrt(a**2 + b**2)

    def plot_triangle(self):
        x = np.array([0, self.a, 0, 0, 0, self.a])
        y = np.array([0, 0, 0, self.b, self.b, 0])
        plt.plot(x, y)
        plt.axis('equal')
        plt.grid()
        plt.show()

triangle1 = RightTriangle(1, 1)
triangle2 = RightTriangle(3, 4)

print(triangle1.c)
print(triangle2.c)

"""
Teminal> python right_triangle.py
1.4142135623730951
5.0
"""

def test_RightTriangle():
    success = False
    try:
        triangle3 = RightTriangle(1,-1)
    except ValueError:
        success = True
    assert success

"""
Teminal> python right_triangle.py
får ValueError
"""

# triangle2.plot_triangle()

"""
Teminal> python right_triangle.py
Plotter trekant
"""
