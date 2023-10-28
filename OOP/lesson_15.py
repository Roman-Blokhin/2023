# Пространство имен класса

JAVA_DEV = 17  # глобальная переменная
JS_DEV = 1


class DepartmentIt:
    PYTHON_DEV = 4
    GO_DEV = 3
    REACT_DEV = 1

    # метод видит глоб. переменную JAVA сразу, а переменные внутри класса не видит, поэтому обращ. к ним через self.
    def info(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV, JAVA_DEV)

    # можно обращаться к переменным в классе через само название класса DepartmentIt
    def info_2(self):
        print(DepartmentIt.PYTHON_DEV, DepartmentIt.GO_DEV, DepartmentIt.REACT_DEV, JS_DEV)

    # можно обращаться как к свойству, через self.
    @property
    def info_3(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    # можно обращаться через декоратор classmethod, вызываем через cls
    @classmethod
    def info_4(cls):
        print("classmethod " + str(cls.PYTHON_DEV), str(cls.GO_DEV), str(cls.REACT_DEV))

    # можно обращаться, через декоратор staticmethod, он ничего не применяет, вызываем через название класса
    @staticmethod
    def info_5():
        print(DepartmentIt.PYTHON_DEV, DepartmentIt.GO_DEV, DepartmentIt.REACT_DEV)

    # как изменяются значения элементов класса, когда мы к ним обращаемся
    def hiring_python_dev(self):
        self.PYTHON_DEV += 1  # мы берем элемент из класса и меняем его, создавая новый ЛОКАЛЬНЫЙ элемент PYTHON_DEV
        DepartmentIt.PYTHON_DEV += 1  # мы меняем значение элемента именно в классе DepartmentIt


it_1 = DepartmentIt()
it_1.info()
it_1.info_2()

it_2 = DepartmentIt()
it_2.info_3  # вызываем как свойство

it_2.info_4()  # вызываем через cls
it_2.info_5()  # вызываем через название класса

it_3 = DepartmentIt()
it_3.hiring_python_dev()
print(it_3.PYTHON_DEV)  # здесь мы обращаемся к новой созданной ЛОКАЛЬНОЙ переменной PYTHON_DEV
print(it_3.__dict__)  # смотрим атрибуты метода hiring_python_dev - видим, какие в нем есть элементы
print(DepartmentIt.PYTHON_DEV)  # обращаемся напрямую к экземпляру класса и меняем его, сохраняя результат
print(DepartmentIt.__dict__)  # смотрим атрибуты всего класса DepartmentIt и видим изменения в переменной PYTHON_DEV