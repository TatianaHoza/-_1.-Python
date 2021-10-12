a = input("Введите строку:").split()
for n, i in enumerate(a):
    if len(i) <= 10:
        print(n, i)
    else:
        print(n, i[:10])

a = [7, 5, 3, 3, 2]
b = float(input("Введите новый элемент рейтинга:"))
i = 0
for n in a:
    if b <= n:
        i = i + 1
    else:
        break
a.insert(i, b)
print(a)