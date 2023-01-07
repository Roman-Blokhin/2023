"""I want to do password generation with tkinter"""

from tkinter import *
import random as r

def generate ():
    a = 10
    chars = ('+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
             'абвгдеёжзийклмнопрстуфхцчшщэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ')
    password = r.sample(chars, a)
    password = ''.join(password)
    name.insert(0, password)
    value = name.get()
    if value [-1:-10] in '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890' \
                         'абвгдеёжзийклмнопрстуфхцчшщэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ':
        name.delete(0, END)
        name.insert(0, password)
        value = name.get()
        print(value)
# TODO: СДЕЛАТЬ, ЧТОБЫ ПОЛЬЗОВАТЕЛЬ МОГ САМ ВЫБИРАТЬ СКОЛЬКО СИМВОЛОВ НУЖНО
# TODO: СДЕЛАТЬ, ЧТОБЫ ПОЛЬЗОВАТЕЛЬ МОГ ВЫБРАТЬ, КАКИЕ СИМВОЛЫ И БУКВЫ ИСПОЛЬЗОВАТЬ

root = Tk ()
root.geometry ('300x100+200+200')
root.title ('Password Generation')
root.configure (bg = 'grey')

Button(text='Generate', bd = 2, command=generate, bg = '#DCDCDC').\
    grid(row=1, column=0, stick = 'wens', padx= 5, pady=5)

name = Entry (root, width = 15, justify=RIGHT, bd = 2, font = ('Arial', 11, 'normal'), bg = '#DCDCDC')
name.grid (row=1, column=1, stick = 'wens', padx= 5, pady=5)

Button (text = 'Clear', bd = 2, bg = '#DCDCDC', command = lambda: name.delete(0, END)).\
    grid(row=2, column=0, stick = 'wens', padx= 5, pady=5)

Label (text='You can generate password for you needs', bg = 'grey', fg = 'white', font = ('Arial', 11, 'normal')).\
    grid (row=0,column=0, columnspan=2)

root.grid_columnconfigure(0, minsize=150)
root.grid_columnconfigure(1, minsize=150)

root.mainloop()