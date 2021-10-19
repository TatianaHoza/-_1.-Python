from functools import reduce
def my_func(el_n,el):
    return el_n * el
print(f'список четных значение от 100 до 1000 {[el for el in range(99,1001) if el % 2 ==0]}')
print(f'произведение всех элементов списка:{reduce(my_func, [el for el in range(99,1001) if el % 2 ==0])}')