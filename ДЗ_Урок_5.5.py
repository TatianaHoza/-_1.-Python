with open("test_5.txt", "w+") as my_file:
    line = input("Введите цифры через пробел \n")
    my_file.writelines(line)
    a = line.split()
print(f'Сумма чисел в файле: {sum(map(int, a))}')