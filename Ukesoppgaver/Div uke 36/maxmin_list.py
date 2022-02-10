a = [1, 2, 3, 4, 5]

def minx(a):
    for i in range(len(a)):
        if a[i] > a[i+1]:
            break
        else:
            print(a[i])
    return
minx(a)

# Koden funker ikke
