"""I want to do the game where you will remember the words"""

import random as r

while True:
    chars = ('+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
             'абвгдеёжзийклмнопрстуфхцчшщэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ')

    conclusion = r.sample (chars, 3)
    conclusion = ''.join(conclusion)
    print ('\n', conclusion)

    answer = input ('\nВведите слово: ')

    if answer == conclusion:
        print ('\nУ вас отличная память!')
    else:
        print ('\nОй! Что-то пошло не так ;)')

    question = input ('\nДля продолжения нажмите Enter, для выхода 0: ')
