my_file = open('test.txt', 'w')
line = ' '
while line:
    my_file.writelines("%s\n" % line)
    if not line:
        break
    line = input('введите строку:\n')
my_file.close()
my_file = open('test.txt', 'r')
content = my_file.read()
print(f'Информация в файле:{content}')
my_file.close()