import sine_f_module as sfm
import math


def table(n_values, alpha_values, T):
    for i in range(len(t)):
        for r in range(len(n)):
            print(f"t = {t[i]:5.3f}, n = {n[r]}, error = {sfm.f(t[i]) - sfm.S(t[i], n[r]):5.4f}")


T = 2 * math.pi
n = [1, 3, 5, 10, 30, 100]
t = [0.01 * T, 0.25 * T, 0.49 * T]

table(n, t, T)

"""
 Put the statements making the table (i.e., the main program from Exercise 3.21) in a separate function
table(n_values, alpha_values, T). 

Make a test block in the module to read T and a series of n and ˛ 
values as positional command-line arguments and make a corresponding call to table.
"""