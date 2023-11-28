import random as r

computer_num = r.randint(0, 10)
point = 3

while True:
    try:
        user_num = int(input('Введите число от 0 до 10: '))
    except ValueError:
        print('Попробуйте еще раз')
        try:
            user_num = int(input('Введите число от 0 до 10: '))
        except ValueError:
            print('Попробуйте еще раз')

    if user_num == computer_num:
        print(f'Вы угадали число! Поздравляем!')
        break
    elif user_num > computer_num:
        print(f'Ваше число: {user_num}, больше..')
    elif user_num < computer_num:
        print(f'Ваше число: {user_num}, меньше....')

    print('Компьютер загадал: ', str(computer_num))

    print(f'Оставшиеся попытки: {point}')

    point -= 1
    if point == 0:
        print('Попыток больше нет. Конец..')
        break

    ret = input('Нажмите Enter ')
