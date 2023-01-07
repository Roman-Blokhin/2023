"""I want to do generation of the password"""

import random as r

chars = ('+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
         'абвгдеёжзийклмнопрстуфхцчшщэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ') # указываем переменную с символами

i = int (input ('Выберите количество символов: '))

password = r.sample (chars, i) # sample отвечает за перемешивание, далее число - сколько символов будет пароль
password = ''.join(password) # прописываем, каким символом будут связаны наши элементы пароля
print (password)