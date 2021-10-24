diction = {}
with open('text_6.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file:
        a, b = line.split(':')
        c = sum(map(int, "".join([i for i in b if i == ' ' or '9' >= i >= '0']).split()))
        diction[a] = c
    print(f'Общее количество часов по предмету - \n {diction}')