# ДЕКОРАТОРЫ 2
# проблема, которая возникает, когда мы делаем декоратор, наша функция теряет свое имя и если
# приобретает имя вложенной функции inner

def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    inner.__name__ = func.__name__  # 5. чтобы после декларации наша функция не теряла имя
    inner.__doc__ = func.__doc__  # 6. чтобы после декларации наша функция не теряла документацию
    return inner


def sqr(x):  # 1. создаем у функции документацию
    """
    Функция возводит в квадрат
    :param x:
    :return:
    """
    print(x ** 2)


print(sqr.__name__)  # 2. здесь мы еще видим имя sqr
help(sqr)  # 3. выводит отформатированную документацию

sqr = table(sqr)  # 4. декорируем функцию sqr
print(sqr.__name__)  # 7. видим имя sqr после декорации и добавления условий №5
help(sqr)  # 8. видим документацию sqr после декорации и добавления условий №6

sqr(5)

# ---------------------------------- #
# Второй способ более короткий

from functools import wraps  # импортируем декоратор wraps


def h_1(func):

    @wraps(func)  # навешиваем декоратор на нашу функц., он напрямую сохр. знач.: __name__ , __doc__ из входной функции
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner


def kwadro(x):
    """
    Это новая функция
    :param x:
    :return:
    """
    print(x ** 2)

kwadro = h_1(kwadro)
kwadro(4)

print(kwadro.__name__)  # выводим имя
help(kwadro)  # выводим документацию