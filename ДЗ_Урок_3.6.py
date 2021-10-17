def int_func():
    for word in input('Введите слово из маленьких латинских букв:').split():
        num = 0
        for c in word:
            if 97 <= ord(c) <= 122:
                num += 1
        print(word.title() if num == len(word) else f"{word}-введите маленькими латинскими буквами")

int_func()

int_func = lambda word: word.title() if word.islower() and ascii(word)[1:-1].isalpha() else ' '
print(' '.join(map(int_func, input("Введите строку из слов из латинских букв:").split())))
