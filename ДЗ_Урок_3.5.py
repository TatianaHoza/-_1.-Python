def adder():
    sum = 0
    while True:
        my_list = input("введите строку чисел или # для завершения программы").split()
        for n in my_list:
            if n.lower() == "#":
                return sum
            else:
                try:
                    sum += int(n)
                except ValueError:
                    print('Для завершения программы введите #')
print(adder())
