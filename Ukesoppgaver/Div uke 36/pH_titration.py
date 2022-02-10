import matplotlib.pyplot as plt
from math import log

# Acid
c_a = 0.3  # M
V_a = 250e-3  # L
n_a = c_a * V_a  # mol
pKa = 4.76

# Base
c_b = 0.5  # M
pKb = 14 - pKa
Kb = 10**(-pKb)


def pH(Vb):
    """ returns the ph after Vb ml of sodium hydroxide is used
     to titrate ethanoic acid"""
    V_b = Vb * 10 ** -3  # L
    n_b = c_b * V_b
    if n_b == 0:
        ph = 0.5 * (pKa - log(c_a, 10))
    elif 0 < n_b < n_a:
        ph = pKa + log(n_b / (n_a - n_b), 10)
    elif abs(n_b - n_a) < 1e-6:
        ph = 14 + 0.5 * log((c_a * c_b) / (c_a + c_b) * Kb, 10)
    else:
        ph = 14 + 0.5 * pKa + log((n_b - n_a) / (V_a + V_b), 10)
    return ph


i = 0
while i <= 200:
    print(i, pH(i))
    i += 5

phs = []
x = []
vol = 0
while vol <= 200:
    phs.append(pH(vol))
    x.append(vol)
    vol += 1e-3

# print(phs)
# print(x)

plt.plot(x, phs)
plt.title("Titration curve: Ethanoic acid and sodium hydroxide")
plt.xlabel("Vol NaOH addded (ml)")
plt.ylabel("pH")
plt.axis(xmin=0, xmax=200)
plt.axis(ymin=0, ymax=16)
plt.grid()
plt.legend(["pH of solution"])
plt.show()


def test_pH():
    vol = 75  # value at equivalence point, ph  = pKa
    expected = pKa
    calculated = pH(vol)
    tol = 1e-10
    success = abs(expected - calculated) < tol
    msg = "pH function fail"
    assert success, msg


"""
============================= test session starts =============================
collecting ... collected 1 item

pH_titration.py::test_pH PASSED                                          [100%]

======================== 1 passed, 1 warning in 1.38s =========================

Process finished with exit code 0
"""