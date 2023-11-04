while True:

    a = int(input('\nВведите первое число: '))
    b = int(input('Введите второе число: '))
    print('\n1. + \n2. - \n3. * \n4. / \n5. Exit')
    c = input('\nВыберите действие: ')

    summ = a + b
    sub = a - b
    mul = a * b
    div = a / b

    if c == '1':
        print(f'Результат: {summ}')

    if c == '2':
        print(f'Результат: {sub}')

    if c == '3':
        print(f'Результат: {mul}')

    if c == '4':
        print(f'Результат: {div}')

    if c == '5':
        print('\nGAME OVER')
        break

    enter = input('\nНажмите Enter, чтобы продолжить, и 1 для выхода: ')

    if enter == '1':
        break
