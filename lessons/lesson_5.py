# Возвращаемое значение функции. Оператор return Python

def square(x):  # создали функцию ,которая возводит число в квадрат
    print(1)
    print(2)
    return x ** 2  # должно быть указано return - то, что возвращает функция, иначе вернет None
    # все, что написано после return не будет возвращаться, потому что функция выходит автоматически


a = square(7)
print(a)


# ------------------------------------ #

def event(y):  # функция проверяет, четное число или нет
    if y % 2 == 0:
        return 'Yes'
    return 'No'


for i in range(1, 10):
    print(i, event(i))


# ------------------------------------ #

def sqPerimetr(c, d):  # функция, которая будет возвращать площадь и периметр
    return c * d, 2 * (c + d)


print(sqPerimetr(4, 9), type(sqPerimetr(4, 9)))  # возвращает в виде кортежа
# если нужно вывести не кортеж, а отдельные числа, то можно создать переменные
square, perimetr = sqPerimetr(2, 6)
print(square, type(square))
print(perimetr)


# ------------------------------------ #

def sqPerimetr(c, d):  # функция, которая будет возвращать список
    list = []
    list.append(c * d)
    list.append(2 * (c + d))
    return list


print(sqPerimetr(5, 8), type(sqPerimetr(5, 8)))  # можно вернуть список
