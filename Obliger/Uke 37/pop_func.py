from math import exp


def N(t, C, k=0.2, B=50000):
    n = B / (1 + C * exp(-k * t))
    return n


for t in range(0, 48 + 1, 4):
    print(f"{t:2}  {N(t, C=(50000/5000) - 1):6.0f}")

"""
Terminal>pop_func.py

 0    5000
 4    9913
 8   17749
12   27526
16   36580
20   42924
24   46552
28   48390
32   49263
36   49666
40   49849
44   49932
48   49970

Process finished with exit code 0
"""