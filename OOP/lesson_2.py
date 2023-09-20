# АТРИБУТЫ КЛАССА

class Person:
    name = 'Roman'  # атрибуты класса
    age = 33


print(Person.name)  # обращаемся к атрибутам класса через точку

print(Person.__dict__)  # посмотреть все атрибуты класса, лучше через python console

print(getattr(Person, 'age'))  # можно обратиться к определенному атрибуту (класс, 'название атрибута')
print(getattr(Person, 'x', 'Нет значения'))  # третьим параметром указываем то, что выведется, если атрибута нет

Person.name = 'Robbie'  # меняем значение атрибута
print(Person.name)

Person.color = 'white'  # добавляем новый атрибут
print(Person.__dict__)

Person.color = 'red'  # меняем значение атрибута
print(Person.color)

setattr(Person, 'color', 'yellow')  # альтернатива замены значения атрибута (класс, 'Имя атрибута', 'новое значение')
print(Person.color)

setattr(Person, 'width', 100)  # создаем новый атрибут для класса
print(Person.__dict__)

del Person.color  # удаление атрибута класса
print(Person.__dict__)

print()
delattr(Person, 'width')  # альтернативное удаление атрибута класса
print(Person.__dict__)
