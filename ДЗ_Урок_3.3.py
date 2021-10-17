def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min(my_list))
    d = sum(my_list)
    return d


a_1 = int(input("Введите число а= "))
a_2 = int(input("Введите число b= "))
a_3 = int(input("Введите число c= "))
print(my_func(a_1, a_2, a_3))

