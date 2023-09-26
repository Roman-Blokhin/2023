# Практика по созданию классов

class Point:
    def __init__(self, coord_x=0, coord_y=0):  # коорд передаем по умолчанию, чтобы не было ошибки при их отсутствии
        self.x = coord_x
        self.y = coord_y

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y