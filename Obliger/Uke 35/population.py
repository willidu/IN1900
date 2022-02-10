from math import exp

B = 50000
k = 0.2

C = (B/5000) - 1
print(f"C = {C}.")

t = 24

print(f"Time is set to {t} hours.")
N = B / (1 + C*exp(-k*t))
print(f"The number of bacteria after {t} hours is {N:.0f}")

"""
Terminal> population.py
C = 9.0.
Time is set to 24 hours.
The number of bacteria after 24 hours is 46552

Process finished with exit code 0
"""