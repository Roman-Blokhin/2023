# Методы экземпляра. Аргумент self


class Cat:
    breed = 'pers'

    def hello(*args):  # принимаем произвольное кол-во аргументов
        print('Hello, Roman', args)

    def show_breed(instance):  # прописываем объект, к которому обращаемся
        print(f'Hello Roman = {instance.breed}')  # обращаемся к объекту через Ф строку


bob = Cat()  # добавляем в класс новый экземпляр

bob.show_breed()  # вызываем метод класса
bob.breed = 'siam' # присваиваем новое значение породы
bob.show_breed()
del bob.breed # удаляем новое значение элемента, возвращаясь к первоначальному значению класса
bob.show_breed()
