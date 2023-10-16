# ДЕКОРАТОРЫ

def decorator(func):  # вкладываем функцию, которую напишем отдельно

    def inner():
        print('Roman')
        func()
        print('is good')

    return inner


def say():
    print('Hello Hero!')


d = decorator(say)
d()
print()

# ДЕКОРАТОРЫ НУЖНЫ, ЧТОБЫ В ФУНКЦИЮ ДОБАВИЛОСЬ НОВОЕ ПОВЕДЕНИЕ ИЛИ ФУНКЦИОНАЛ

say = decorator(say)  # создали декоратор, переменную называем по имени функции, которую вызываем
say()
print(say)  # как мы можем проверить, что переменная задекорирована, видим, что вложена функция inner


# ------------------------------------------ #

# Если нам нужно передать аргументы в функцию, лучше всегда использовать *args, **kwargs

def decorator(func):
    def inner(*args, **kwargs):  # 1. принимает любое количество переданных аргументов
        print('Roman')
        func(*args, **kwargs)  # 2. принимает любое количество переданных аргументов
        print('is good')

    return inner


def say(name, surname, age):  # 3. передаем аргументы
    print('Hello Hero!', name, surname, age)  # 4. выводим аргументы


say = decorator(say)
say('Rob', 'Waters', 16)  # 5. прописываем значение аргументов
print()

# ------------------------------------------ #

# Если нам нужно передать аргументы в функцию, лучше всегда использовать *args, **kwargs

def header(func):  # 2. создали первый декоратор
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')

    return inner

def table(func):  # 2. создали второй декоратор
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner

@header  # 3. навесили декоратор, который будет сверху
@table  # 4. такая надпись с @ заменяет: say = header(table(say))
def say(name, surname, age):
    print('Hello Hero!', name, surname, age)


# say = decorator(say)  # 5. убираем лишнее
say('Rob', 'Waters', 16)
