# ПРАКТИКА С property

class User:
    def __init__(self, login, password):
        self.login = login
        self.__password = password

    @property
    def password (self):
        return self.__password

    @password.setter
    def password (self, value):
        self.__password = value