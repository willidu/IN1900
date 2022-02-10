def myfactorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        s = 1
        while n > 1:
            s *= n
            n -= 1
        return s


from math import factorial

test = myfactorial(5) == factorial(5)
if test is True:
    print("Programmet funker")
