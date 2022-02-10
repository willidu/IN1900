from math import pi

h = 5.0  # height
b = 2.0  # base
r = 1.5  # radius
area_para = h * b
print(f"The area of the parallelogram is {area_para:g}")
area_square = b ** 2
print(f"The area of the square is {area_square:g}")
area_circle = pi * r ** 2
print(f"The area of the circle is {area_circle:.3f}")
volume_cone = 1.0 / 3 * pi * r ** 2 * h
print(f"The volume of the cone is {volume_cone:.3f}")
