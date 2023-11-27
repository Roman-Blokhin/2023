import random as r

while True:
    user_num = int(input('Введите число от 0 до 10: '))
    computer_num = r.randint(0, 10)

    print('Компьютер загадал: ', str(computer_num))

    if user_num == computer_num:
        print(f'Вы угадали число!')
    elif user_num > computer_num:
        print(f'Ваше число {user_num} больше..')
    elif user_num < computer_num:
        print(f'Ваше число {user_num} меньше....')

    ret = input('Нажмите Enter')
