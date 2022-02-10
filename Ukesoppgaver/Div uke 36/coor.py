liste = []
n = 10
a = 0
b = 100
h = (b - a) / n

for i in range(n+1):
    liste.append(int(a+i*h))
print(liste)
