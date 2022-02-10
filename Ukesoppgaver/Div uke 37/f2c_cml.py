import sys
print(sys.argv[1])

f = int(sys.argv[1])
c = (f - 32) * (5 / 9)
print(f"{f} Fahrenheit is {c:.2f} degrees Celsius")
