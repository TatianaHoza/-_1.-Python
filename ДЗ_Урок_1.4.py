n = int(input("Введите целое число:"))
i = 0
while n > 0:
    a = n % 10
    if a >= i:
        i = a
    n = n//10
print(i)