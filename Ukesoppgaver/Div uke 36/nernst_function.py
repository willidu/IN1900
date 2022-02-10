from math import log

q = ((0.0656**2 * 0.192 **2) / ())

def E_cell(E0cell, n, Q, T=273.15):
    F = 1.60e-19 * 6.02e23
    E = E0cell - ((8.314 * T)/(n * F)) * log(Q)
    return E


# Finner ikke ut av hva Q skal være så får ikke gjort moe mer
