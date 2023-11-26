# Магические методы __iter__ и __next__
# производит итерацию(поочередный вызов значений при вызове функции) наших аргументов

class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __iter__(self):  # производит итерацию аргумента нашего элемента
        return iter(self.surname)  # возвращаем итератор у типа строки

igor = Student('Igor', 'Nikolaev', [1, 2, 3, 4, 5])
for i in igor:
    print (i)

# если мы хотим производить итерацию не элемента, а класса, то нам нужно:

class Student_2:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __iter__(self):
        self.index = 0  # 2. создаем атрибут index, 0 - первая буква нашего имени
        return iter(self.surname)

    def __next__(self):  # 1. создаем новую функцию
        letter = self.name[self.index]  # 3. делаем переменную, куда сохраняем нашу первую букву, чтобы ее не потерять
        self.index +=1  # 4. увеличиваем индекс на 1
        return letter # 3. возвращаем с первой буквы

bob = Student_2('Bob', 'Romanov', [1, 2, 3, 4, 5])
for i in bob:
    print (i)