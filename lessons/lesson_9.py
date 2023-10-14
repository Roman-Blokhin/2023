# Замыкания часть 2
# создаем функцию, которая будет подсчитывать среднее значение

def average_numbers():
    number = []  # создаем пустой список

    def inner(num):
        number.append(num)  # добавляем новый аргумент в список
        print(number)
        return sum(number) / len(number)  # возвращаем среднее значение от суммы чисел

    return inner


# ------------------------------------------ #

def average():
    summa = 0
    count = 0

    def inner(num):
        nonlocal summa  # изменяем переменную в соседней зоне видимости
        nonlocal count
        summa = summa + num
        count += 1
        print(summa, count)

        return summa / count

    return inner


# ------------------------------------------ #

from time import perf_counter  # импортируем функцию, которая запускает таймер в секундах


def timer():
    start = perf_counter()  # при первом вызове функции фиксирует время (включает таймер)

    def inner():  # функция вызовет разницу времени между первым вызовом функции и последним
        return round(perf_counter() - start)  # округляем до целых чисел

    return inner


# ------------------------------------------ #

def add(a, b):  # пишем функцию для вызова
    return a + b


def counter(func):  # определяем функцию ,которая будет вести счет и показывать результат
    count = 0

    def inner(*args, **kwargs):  # принимает все переданные аргументы (их может быть произвольное кол-во)
        nonlocal count
        count += 1
        print(f"Вызвана функция {func.__name__} {count} раз")  # func.__name__ - позволяет вывести имя функции
        return func(*args, **kwargs)

    return inner
