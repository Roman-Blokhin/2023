# Пространство имен класса

JAVA_DEV = 17  # глобальная переменная


class DepartmentIt:
    PYTHON_DEV = 4
    GO_DEV = 3
    REACT_DEV = 1

    # метод видит глоб. переменную JAVA сразу, а переменные внутри класса не видит, поэтому обращ. к ним через .self
    def info(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV, JAVA_DEV)


it_1 = DepartmentIt()
it_1.info()