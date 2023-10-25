# ПРАКТИКА С property

class User:
    def __init__(self, login, password):
        self.__login = login
        self.__password = password

    @property
    def password (self):
        return self.__password

    @password.setter
    def password (self, value):
        if not isinstance(value, str):
            raise TypeError ('Пароль должен быть текстом')
        if len(value) < 4:
            raise ValueError ('Длина пароль не может быть меньше 4 символов')
        if len(value) > 10:
            raise ValueError ('Длина пароль не может быть больше 10 символов')
        self.__password = value

    @property
    def login (self):
        return self.__login

    @login.setter
    def login (self, value):
        self.__login = value

