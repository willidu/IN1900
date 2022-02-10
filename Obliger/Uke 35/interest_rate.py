P = 1000
r = 5
n = 0

while n < 3:
    A = P * (1 + r / 100) ** n
    n += 1

print(f"The value has grown to {A} euros after {n} years")

"""
Terminal> python interest_rate.py
The value has grown to 1102.5 euros after 3 years

Process finished with exit code 0
"""