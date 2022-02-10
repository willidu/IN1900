import os

path = "C:/Users/Administrator/PycharmProjects/IN1900/Obliger/Ukesoppgaver/Uke 38/"
filename = os.path.join(path, "oxygen.txt")

with open(filename, "r") as file:
    file.readline()
    w = []
    m = []
    for line in file:
        lines = line.split()
        w.append(float(lines[-1]))
        m.append(float(lines[1]))

s = 0
for i in range(len(w)):
    s += m[i]*w[i]
print(f"M = {s:.4f} g/mol")

"""
Terminal> python read_file_isotopes.py
M = 15.99937 g/mol
"""