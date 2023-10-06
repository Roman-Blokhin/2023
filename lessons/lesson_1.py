# ООП, РАЗБИРАЕМСЯ В КЛАССАХ

class Dog: # создали класс
    name = None # создаем поля(переменные) для будущих значений
    age = None
    isHappy = None

    def set_data(self, name, age, isHappy): # метод, он поможет сократить определение данных в новых объектах
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self): # создали метод, который выводит все параметры объекта
        print('Имя:', self.name, 'Возраст:', self.age, 'Счастье:', self.isHappy )

dog_1 = Dog() # создаем объект на основе класса
dog_1.set_data('Robbie', 1.5, True) # используем метод в нашем классе

dog_2 = Dog() # используем поля/переменные в нашем классе
dog_2.name = 'William'
dog_2.age = 4
dog_2.isHappy = False

print(dog_1.isHappy) # выводим частичную информацию через поле(переменную)
print(dog_2.name)

dog_1.get_data() # выводим всю информацию через метод
dog_2.get_data()

