import os
path = "C:/Users/Administrator/PycharmProjects/IN1900/Ukesoppgaver/Div uke 37/"
filename = os.path.join(path, "newton_objects.txt")

with open(filename, "r") as file:  # åpner fil som 'file'
    m = []                         # tom liste hvor vi skal plassere masseverdiene
    r = []                         # tom liste hvor vi skal plassere avstandsverdiene
    for line in file:              # for line (linje) in file (filen vi leser fra)
        lines = line.split()       # deler opp linjen
        # print(lines)
        m.append(float(lines[0]))  # legger til første del av linjen som flyttall i m
        r.append(float(lines[1]))  # legger til siste del av linjen som flyttall i r

print(m, r)
