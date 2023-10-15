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
print(say)  # иак мы можем проверить, что переменная задекорирована, видим, что вложена функция inner