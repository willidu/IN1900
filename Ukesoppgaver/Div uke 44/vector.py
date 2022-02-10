class Vector2D:
    def __init__(self, a , b):
        self.a = a
        self.b = b
    
    def __add__(self, other):
        a_new = self.a + other.a
        b_new = self.b + other.b
        return Vector2D(a_new, b_new)

    def __sub__(self, other):
        a_new = self.a - other.a
        b_new = self.b - other.b
        return Vector2D(a_new, b_new)

    def dot(self, other):
        return self.a*other.a + self.b*other.b

    def __str__(self):
        return f'({self.a}, {self.b})'

v1 = Vector2D(1, 2)
v2 = Vector2D(-2, 5)
"""
print(v1, v2)
print(v1+v2)
print(v1-v2)
print(v1.dot(v2))
"""

class Vector3D:
    def __init__(self, a, b, c):
        Vector2D.__init__(self, a, b)
        self.c = c

    def __add__(self, other):
        a_new = self.a + other.a
        b_new = self.b + other.b
        c_new = self.c + other.c
        return Vector3D(a_new, b_new, c_new)

    def __sub__(self, other):
        a_new = self.a - other.a
        b_new = self.b - other.b
        c_new = self.c - other.c
        return Vector3D(a_new, b_new, c_new)

    def dot(self, other):
        return Vector2D.dot(self, other) + self.c*other.c

    def __str__(self):
        return f'({self.a}, {self.b}, {self.c})'

    def cross(self, other):
        c1 = self.b*other.c - self.c*other.b
        c2 = self.c*other.a - other.a*self.c
        c3 = self.a*other.b - self.b*other.a
        return Vector3D(c1, c2, c3)

v3 = Vector3D(1, 2, 4)
v4 = Vector3D(-2, 5, 1)
"""
print(v3.dot(v4))
print(v3+v4)
"""

v = Vector3D(2, 0, 0)
w = Vector3D(0, 2, 0)
print(v.cross(w))
