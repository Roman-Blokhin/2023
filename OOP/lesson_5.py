# Методы экземпляра. Аргумент self


class Cat:
    breed = 'pers'

    def hello(*args):  # принимаем произвольное кол-во аргументов
        print('Hello, Roman', args)

    def show_breed(instance):  # прописываем объект, к которому обращаемся
        print(f'Hello Roman = {instance.breed}')  # обращаемся к объекту через Ф строку

    def show_name(instance):  # прописываем объект, к которому обращаемся
        if hasattr(instance, 'name'):  # делаем проверку, есть ли аттрибут в классе
            print(f'Name = {instance.name}')  # обращаемся к объекту через Ф строку
        else:
            print('Такого аттрибута нет')

    def set_value (koshka, value, num=0): # первый аргумент - наш объект, второй арг. - значение
        koshka.name = value # присваиваем объекту аргумент и значение
        koshka.age = num # задаем возврат по умолчанию в аргументах метода


bob = Cat()  # добавляем в класс новый экземпляр

bob.show_breed()  # вызываем метод класса
bob.breed = 'siam'  # присваиваем новое значение породы
bob.show_breed()
del bob.breed  # удаляем новое значение элемента, возвращаясь к первоначальному значению класса
bob.show_breed()

# bob.name = 'Robert' # присваиваем новый атрибут нашему элементу
bob.show_name()  # если имя дополнительно не назначено, будет ошибка. Нужна проверка hasattr() в методе

tom = Cat()
tom.set_value('Tom') # первый аргумент не пишем, потому что он считывает наш объект, пишем значение, как в методе
print (tom.name)
print(tom.age)
