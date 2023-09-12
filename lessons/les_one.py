# ООП, РАЗБИРАЕМСЯ В КЛАССАХ

class Dog: # создали класс
    name = None # создаем поля(переменные) для будущих значений
    age = None
    isHappy = None

dog_1 = Dog() # создаем объект на основе класса
dog_1.name = 'Robbie'
dog_1.age = 1.5
dog_1.isHappy = True

dog_2 = Dog()
dog_2.name = 'William'
dog_2.age = 4
dog_2.isHappy = False

print(dog_1.name)
print(dog_2.name)

