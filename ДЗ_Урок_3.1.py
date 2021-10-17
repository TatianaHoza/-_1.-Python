def my_func():
    try:
        a = int(input("Введите число а="))
        b = int(input("Введите число b="))
        c = a/b
    except ValueError:
        return "ValueError"
    except ZeroDivisionError:
        return "На ноль делить нельзя, введите другое значение b"
    return c
print(my_func())
