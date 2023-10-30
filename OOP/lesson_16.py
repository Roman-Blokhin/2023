# Магические методы. Методы __str__ и __repr__ - отвечают за текстовое отображение в нашей системе

class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):  # отвечает за то, как будут отображаться данные для разработчиков
        return f'Объект Lion - {self.name}'  # показываем, что будет в описании объекта в backend

a = Lion('Roman')
print(a)  # выводит Объект Lion - Roman, а не: <__main__.Lion object at 0x0000022113133310>, как раньше