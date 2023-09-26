# Практика по созданию классов

class Point:
    def __init__(self, coord_x=0, coord_y=0):  # коорд передаем по умолчанию, чтобы не было ошибки при их отсутствии
        self.move_to(coord_x, coord_y)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)  # используем уже созданный метод для упрощения кода