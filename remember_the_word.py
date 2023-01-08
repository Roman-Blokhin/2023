"""I want to do the game where you will be remember the words"""

import random as r

chars = ('+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
         'абвгдеёжзийклмнопрстуфхцчшщэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ')

conclusion = r.sample (chars, 5)
conclusion = ''.join(conclusion)
print (conclusion)
