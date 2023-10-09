# Вложенные функции Python

g = 'gray'  # глобальная переменна


def colors():
    y = 'yellow'  # объемлющая переменная
    g = 'green'

    def print_red():
        nonlocal y  # позволяет менять объемлющую переменную
        r = 'red'  # локальная переменная в функции
        print(r, y, g)
        y = 'changed'

    def print_blue():
        b = 'blue'
        print(b, y, g)

    print_red()
    print_blue()


colors()
