# Методы экземпляра. Аргумент self


class Cat:
    def hello (self):
        print ('Hello, Roman')

a = Cat()
print(Cat.hello(a))