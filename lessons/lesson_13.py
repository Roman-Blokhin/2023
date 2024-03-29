# Форматирование строк: метод format и F-строки

name = 'Roman'
age = "33"
age_2 = 33
print('1. Меня зовут ' + name + ', мне ' + age + ' года')  # простой вывод информации

# используем метод .format()
life = '2. Мое имя: {0}, {1} года, я - {0}'.format(name, age)  # аргументы считываются по индексу и вставляются в текст
print(life)

# используем метод .format() с переменными в аргументах
life_2 = '3. Родители назвали: {fio}, {old} года назад, имя: {fio}'.format(fio=name, old=age)
print(life_2)


# F - строка
# не нужно подставлять методы, просто прописываем переменные в f строке
print(f'4. Мое имя: {name}, {age} года, я - {name}')

# для переменных мы можем вызывать любые методы и действия
print(f'5. Имя: {name.upper()}, {age_2*3} лет, я - {name.lower()}. В моем имени {len(name)} букв')