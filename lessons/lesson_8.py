# Замыкания в Python

def one(value):
    name = value  # ы создаем переменную со значением, которое будет связано с функцией в конкретном вызове

    def two():
        print('HELLO ROMAN', name)

    return two  # возвращаем значение функций, потому что без return будет значение NONE


a = one('Mister')  # присваиваем функцию переменной

a()  # вызываем функцию

b = one('Missis')  # каждый раз задается новое значение, не влияющее на прошлый вызов

b()


# -------------------------- #

def adder(value):
    def inner(a):
        return value + a

    return inner


instance = adder(5)  # мы присвоили значение 5 нашей функции adder(value), оно запомнилось системой
print(instance(10))  # а здесь мы задаем значение нашей вложенной функции inner(a)

example = adder(100)
print(example(1000))


# -------------------------- #

def counter():
    count = 0

    def one():
        nonlocal count  # обращаемся к объемлющей переменной count и определяем область видимости, меняя ее
        count += 1  # действие с переменной
        return count  # возвращаем переменную count

    return one  # возвращаем результат функции


value = counter()  # присваиваем переменной функцию counter
print(value())  # вызываем функцию через переменную
print(value())
print(value())  # значение у нас сохраняется, сколько раз вызывали счетчик
