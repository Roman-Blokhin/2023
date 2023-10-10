# Замыкания в Python

def one():
    def two():
        print('HELLO ROMAN')

    return two  # возвращаем значение функций, потому что без return будет значение NONE

a = one()  # присваиваем функцию переменной

a()  # вызываем функцию