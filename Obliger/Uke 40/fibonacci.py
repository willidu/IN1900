x = [0, 1]
for n in range(len(x), 15):
    x.append(x[n-1] + x[n-2])

print(f"The first {len(x)} Fibonacci numbers are \n{x}")

"""
Terminal> python fibonacci.py
The first 15 Fibonacci numbers are 
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
"""