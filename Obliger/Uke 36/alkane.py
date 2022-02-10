Mc = 12.011  # g/mol
Mh = 1.0079  # g/mol

for n in range(2, 10):
    m = 2 * n + 2
    M = n * Mc + m * Mh
    print(f"M(C{n}H{m}) = {M:6.3f} g/mol")

"""
Terminal> alkane.py
M(C2H6) = 30.069 g/mol
M(C3H8) = 44.096 g/mol
M(C4H10) = 58.123 g/mol
M(C5H12) = 72.150 g/mol
M(C6H14) = 86.177 g/mol
M(C7H16) = 100.203 g/mol
M(C8H18) = 114.230 g/mol
M(C9H20) = 128.257 g/mol

Process finished with exit code 0
"""
