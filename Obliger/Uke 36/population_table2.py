from math import exp

n = 12
t = [0] * (n + 1)
N = [0] * (n + 1)

B = 50000
k = 0.2
C = (B / 5000) - 1

t0 = 0
t_max = 48
h = (t_max - t0) / n

for i in range(n + 1):
    t[i] = i * h
    N[i] = bac = B / (1 + C * exp(-k * i * h))
    # print(f"{i:2}  {bac:5.0f}")

tN1 = [t, N]
for i in range(len(tN1[0])):
    print(f"{tN1[0][i]:2.0f}  {tN1[1][i]:5.0f}")
    # print(tN1[0][i], tN1[1][i])

print("---------------------------------------------")

tN2 = [0] * (n + 1)
for i in range(len(t)):
    tN2[i] = [tN1[0][i], tN1[1][i]]

for i in range(len(tN2)):
    print(f"{tN2[i][0]:2.0f}  {tN2[i][1]:5.0f}")

"""
Terminal> population_table2.py
 0   5000
 4   9913
 8  17749
12  27526
16  36580
20  42924
24  46552
28  48390
32  49263
36  49666
40  49849
44  49932
48  49970
---------------------------------------------
 0   5000
 4   9913
 8  17749
12  27526
16  36580
20  42924
24  46552
28  48390
32  49263
36  49666
40  49849
44  49932
48  49970

Process finished with exit code 0
"""
