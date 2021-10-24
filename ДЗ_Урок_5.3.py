with open('text_3.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file:
        dictionary = {line.split()[0]: float(line.split()[1])}
        print(f'Средний оклад {round(sum(dictionary.values()) / len(dictionary), 3)}\n'
              f'Оклад меньше 20.000 {[i[0] for i in dictionary.items() if i[1] < 20000]}')
