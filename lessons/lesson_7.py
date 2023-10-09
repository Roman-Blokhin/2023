# Вложенные функции Python

def colors():
    def print_red():
        r = 'red'
        print(r)

    def print_blue():
        b = 'blue'
        print(b)

    print_red()
    print_blue()


colors()
