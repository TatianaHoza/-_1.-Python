import json
with open("text_77.json", 'w', encoding='utf-8') as my_file:
    with open('text_7.txt', encoding='utf-8') as my_file_1:
        a = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in my_file_1}
        b = [a, {'средняя прибыль': round(sum([int(i) for i in a.values() if int(i) > 0]) /
                                          len([int(i) for i in a.values() if int(i) > 0]))}]
        json.dump(b, my_file, ensure_ascii=False, indent=4)
