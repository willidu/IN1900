s = 0
M = 3

for k in range(1, M+1):  # k in range instead of i, (1, M+1) as range instead of (M)
    s += 1 / (2 * k) ** 2  # missing parentheses

print(s)

"""
Terminal> sum_for.py
0.3402777777777778

Process finished with exit code 0
"""