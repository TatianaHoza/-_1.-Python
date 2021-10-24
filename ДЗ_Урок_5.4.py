from googletrans import Translator

with open("text_4_translate.txt", 'w', encoding='utf-8') as my_file:
    with open("text_4.txt", 'r', encoding='utf-8') as my_file_1:
        content = my_file_1.read()
    try:
        my_file.write(Translator().translate(content, dest='ru').text)
        print(Translator().translate(content, dest='ru').text)
    except AttributeError:
        print("Ошибка!")