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
