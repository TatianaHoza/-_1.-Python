a = input("Введите строку:").split()
for n, i in enumerate(a):
    if len(i) <= 10:
        print(n, i)
    else:
        print(n, i[:10])
