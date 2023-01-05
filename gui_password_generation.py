"""I want to do password generation with tkinter"""

from tkinter import *
import random as r

def generate ():
    chars = ('+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
             'абвгдеёжзийклмнопрстуфхцчшщэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ')
    password = r.sample(chars, 10)
    password = ''.join(password)
    name.insert(0, password)
    value = name.get()
    print (value)

root = Tk ()
root.geometry ('200x200+200+200')
root.title ('Password Generation')

Button(text='Generate', bd = 2, command=generate).\
    grid(row=0, column=0, stick = 'wens', padx= 5, pady=5)

name = Entry (root, width = 15, justify=RIGHT, bd = 2)
name.grid (row=0, column=1, stick = 'wens', padx= 5, pady=5)

Button (text = 'Clear', bd = 2, command = lambda: name.delete(0, END)).\
    grid(row=1, column=0, stick = 'wens', padx= 5, pady=5)

root.grid_columnconfigure(0, minsize=80)
root.grid_columnconfigure(1, minsize=80)

root.mainloop()