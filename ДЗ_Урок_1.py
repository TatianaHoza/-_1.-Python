name = input("Введите ФИО пациента:")
age = input("Введите дату рождения:")
doza = int(input("Доз вакцины сделано:"))
if doza==2:
    print("Сертификат о вакцинации выдан пациенту: ",name, age)
else:
    print(name, "не прошёл полный курс вакцинации")