from sys import argv
def my_func():
    try:
        a, b, c = map(float, argv[1:])
        d = a * b + c
        print(f'заработная плата сотрудника  {d}')
    except ValueError:
        return print('Not a number')


my_func()