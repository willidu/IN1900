import math

print("Oppgave tilsier a = 6, b = -5, c = 1")

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

d = (b ** 2 - 4 * a * c)
if (b ** 2 - 4 * a * c) < 0:
    print("No real roots")
else:
    x_1 = -b + math.sqrt(d) / (2 * a)
    x_2 = -b - math.sqrt(d) / (2 * a)
print(f"x_1 = {x_1:.2f}")
print(f"x_2 = {x_2:.2f}")

"""
Terminal> python find_roots.py

x_1 = 5.08
x_2 = 4.92

Process finished with exit code 0
"""