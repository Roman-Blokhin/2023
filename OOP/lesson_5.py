# Методы экземпляра. Аргумент self


class Cat:
    breed = 'pers'

    def hello(*args):  # принимаем произвольное кол-во аргументов
        print('Hello, Roman', args)

    def show_breed(instance):  # прописываем объект, к которому обращаемся
        print(f'Hello Roman = {instance.breed}')  # обращаемся к объекту через Ф строку


bob = Cat()  # добавляем в класс новый экземпляр

bob.show_breed()  # вызываем метод класса
