# Магические методы __iter__ и __next__
# производит итерацию(поочередный вызов значений при вызове функции) наших аргументов

class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

igor = Student('Igor', 'Nikolaev', [1,2,3,4,5])
for i in igor:
    print (i)