my_file = open("task_2.txt", 'r', encoding='utf-8')
content = my_file.read()
print(content)
my_file.close()
with open("task_2.txt", encoding='utf-8') as my_file:
    content = my_file.readlines()
    size = len(content)
    print(f'\nКоличество строк в файле:{size}')
    for i in range(len(content)):
        print(f'Количество символов {i+1} строки - {len(content[i])}')
    for i in range(len(content)):
        print(f'Количество слов {i+1} строки - {len(content[i].split())}')