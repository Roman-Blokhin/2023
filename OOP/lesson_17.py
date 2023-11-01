# Магические методы __len__ и __abs__

class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __len__(self):  # функция, которая будет считать количество символов всех атрибутов наших экземпляров
        return len(self.name + self.surname)
