from colorama import Fore, Back, Style

popitka = 1

while True:
    print(Fore.RED + f'\nДействие: {popitka}' + Style.RESET_ALL)
    try:
        a = int(input('\nВведите первое число: '))
    except ValueError:
        print(Fore.BLUE + '\nВы не ввели число' + Style.RESET_ALL)
        try:
            a = int(input('\nВведите первое число: '))
        except ValueError:
            print(Fore.BLUE + '\nНу, как знаете.. До свидания.' + Style.RESET_ALL)
            break

    try:
        b = int(input('Введите второе число: '))
    except ValueError:
        print(Fore.BLUE + '\nВы не ввели число' + Style.RESET_ALL)
        try:
            b = int(input('\nВведите второе число: '))
        except ValueError:
            print(Fore.BLUE + '\nНу, как знаете.. До свидания.' + Style.RESET_ALL)
            break

    print('\n1. + \n2. - \n3. * \n4. / \n5. Exit')
    c = input('\nВыберите действие: ')

    summ = a + b
    sub = a - b
    mul = a * b
    div = a / b

    if c == '1':
        print(f'Результат: ' + Fore.YELLOW + f'{summ}' + Style.RESET_ALL)

    if c == '2':
        print(f'Результат: ' + Fore.YELLOW + f'{sub}' + Style.RESET_ALL)

    if c == '3':
        print(f'Результат: ' + Fore.YELLOW + f'{mul}' + Style.RESET_ALL)

    if c == '4':
        print(f'Результат: ' + Fore.YELLOW + f'{div}' + Style.RESET_ALL)

    if c == '5':
        print(Fore.RED + '\nДо свидания' + Style.RESET_ALL)
        break

    enter = input('\nНажмите ' + Fore.BLUE + 'Enter' + Style.RESET_ALL + ', чтобы продолжить, или '
                  + Fore.BLUE + '1' + Style.RESET_ALL + ' для выхода: ' + Style.RESET_ALL)

    if enter == '1':
        print(Fore.RED + '\nДо свидания' + Style.RESET_ALL)
        break

    popitka +=1
