# БИЛЕТЫ ДЛЯ МОЕЙ ПРОГРАММЫ С ЭКЗАМЕНОМ ДЛЯ СОБЕСЕДОВАНИЯ

"""
Бэкенд. Набрать страницу из разных элементов (заголовки, картинки, списки, голосовалки, квоты).
Бизнес логика. Описать классы самой страницы и отдельно объектов на ней.
"""

import base64  # импортируем кодировщик


class Text:  # родительский класс для текста
    def __init__(self, text):
        self.text = text


class Image:  # класс, в котором храним картинку, закодированную в base64
    def __init__(self, image):
        self.image: base64 = image


class Comment(Text):  # наследуем параметры инициализации от класса Text
    def person(self, author):
        self.author = author


# --------------------- #
'''
1. Как добавить объект на страницу (создаем список, далее метод добавления в список объекта). 
Нужно отобразить объект на странице (с помощью джойна)
2. Что за магические методы __str__ и __repr__ , в чем их разница? Реализуйте их в классе
'''

class Page:
    def __init__(self, name):
        self.obj_list = []
        self.name = name

    def __repr__(self):
        return f'Объект: {self.name}'

    def __str__(self):
        return f'Имя: {self.name}'

    def add(self, obj):
        self.obj_list.append(obj)

    def show(self):
        return ' '.join(f'{self.obj_list}')
