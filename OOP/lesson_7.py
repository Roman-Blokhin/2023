# Практика по созданию классов

class Point:
    def __init__(self, coord_x=0, coord_y=0):  # коорд передаем по умолчанию, чтобы не было ошибки при их отсутствии
        self.coord_x = coord_x
        self.coord_y = coord_y

