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
