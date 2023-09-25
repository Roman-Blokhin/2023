# Инициализация объекта. Метод init

class Dog:
    # создаем метод инициализации, через который передаем аргументы нашему новому объекту в классе
    # он нужен, чтобы заполнять объект значениями
    def __init__(self, color, name, age=4, breed='siam'):
        self.name = name
        self.age = age
        self.color = color
        self.breed = breed

rob = Dog('black', 'ROB') # передаем параметры, которых нет, аргумент self считывает название создаваемого объекта
print(rob.name)
print(rob.color)
print(rob.age)
print(rob.breed)
print()

# создаем новый объект
kelly = Dog('white', 'Kelly', age = 2) # мы можем изменять параметры, которые проставлены по умолчанию
print(kelly.name)
print(kelly.color)
print(kelly.age)
print(kelly.breed)

# создаем новый объект
rom = Dog('red', 'Roman', age = 33) # мы можем изменять параметры, которые проставлены по умолчанию
print(rom.name)
print(rom.color)
print(rom.age)
print(rom.breed)
rom.engine = 7
print(rom.engine)


