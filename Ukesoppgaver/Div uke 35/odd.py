n = int(input("n = ? \n"))
k = 1
for num in range(k, n + 1):
    if num % 2 != 0:
        print(num, end=" ")  # end=" " setter de på linje med 1 mellomrom
