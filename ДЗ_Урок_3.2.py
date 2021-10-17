def my_func(**kwargs):
    return ' '.join(kwargs.values())
print(my_func(Firstname=input("Введите имя:"), Lastname=input("Введите фамилию:"), Age=input("Введите год рождения:"),
              Town=input("Введите город проживания:"), Email=input("Введите email:"), Phone=input("Введите телефон:")))