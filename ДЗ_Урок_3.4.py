def my_func():
    x = float(input("Введите целое положительное число x="))
    y = int(input("Введите отрицательное число y="))
    if y >= 0:
        print("y должно быть отрицательным")
    else:
        a = x ** y
        return a
print(my_func())
