s = 0
M = 3
k = 1

while k <= M:
    s += 1 / (2 * k) ** 2
    k += 1

print(s)

"""
Terminal> sum_while.py
0.3402777777777778

Process finished with exit code 0
"""