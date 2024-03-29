"""I want to do password generation with tkinter"""

from tkinter import *
import random as r

# ------------------------------------------------------------- GENERATE ZONE - DEF

def generate ():
    a = 10

    if one_value.get () == 0 and two_value.get () == 0 and three_value.get () == 0:
        name.delete(0, END)
        name.insert(0, 'ERROR')
        value = name.get()

    elif one_value.get() == 1 and two_value.get() == 1 and three_value.get() == 1:
        chars = ('+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
        password = r.sample(chars, a)
        password = ''.join(password)
        name.insert(0, password)
        value = name.get()
        if value[-1:-10] in '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890':
            name.delete(0, END)
            name.insert(0, password)
            value = name.get()

    elif one_value.get() == 1 and two_value.get() == 0 and three_value.get() == 0:
        chars = ('abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        password = r.sample(chars, a)
        password = ''.join(password)
        name.insert(0, password)
        value = name.get()
        if value[-1:-10] in '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890':
            name.delete(0, END)
            name.insert(0, password)
            value = name.get()

    elif one_value.get() == 0 and two_value.get() == 1 and three_value.get() == 0:
        chars = ('+-/*!&$#?=@<>')
        password = r.sample(chars, a)
        password = ''.join(password)
        name.insert(0, password)
        value = name.get()
        if value[-1:-10] in '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890':
            name.delete(0, END)
            name.insert(0, password)
            value = name.get()

    elif one_value.get() == 0 and two_value.get() == 0 and three_value.get() == 1:
        chars = ('1234567890')
        password = r.sample(chars, a)
        password = ''.join(password)
        name.insert(0, password)
        value = name.get()
        if value[-1:-10] in '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890':
            name.delete(0, END)
            name.insert(0, password)
            value = name.get()

    elif one_value.get() == 1 and two_value.get() == 1 and three_value.get() == 0:
        chars = ('+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        password = r.sample(chars, a)
        password = ''.join(password)
        name.insert(0, password)
        value = name.get()
        if value[-1:-10] in '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890':
            name.delete(0, END)
            name.insert(0, password)
            value = name.get()

    elif one_value.get() == 1 and two_value.get() == 0 and three_value.get() == 1:
        chars = ('abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
        password = r.sample(chars, a)
        password = ''.join(password)
        name.insert(0, password)
        value = name.get()
        if value[-1:-10] in '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890':
            name.delete(0, END)
            name.insert(0, password)
            value = name.get()

    elif one_value.get() == 0 and two_value.get() == 1 and three_value.get() == 1:
        chars = ('+-/*!&$#?=@<>1234567890')
        password = r.sample(chars, a)
        password = ''.join(password)
        name.insert(0, password)
        value = name.get()
        if value[-1:-10] in '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890':
            name.delete(0, END)
            name.insert(0, password)
            value = name.get()

    print(value)
    print('1.', one_value.get())
    print('2.', two_value.get())
    print('3.', three_value.get())

# ------------------------------------------------------------- OTHER DEF

def select_all ():
    for i in [one, two, three]:
        i.select ()

def deselect_all ():
    for i in [one, two, three]:
        i.deselect ()

# ------------------------------------------------------------- TASK

# TODO: СДЕЛАТЬ, ЧТОБЫ ПОЛЬЗОВАТЕЛЬ МОГ САМ ВЫБИРАТЬ СКОЛЬКО СИМВОЛОВ НУЖНО

# ------------------------------------------------------------- WINDOW

root = Tk ()
root.geometry ('330x230+200+200')
root.title ('Password Generation')
root.configure (bg = 'grey')

# ------------------------------------------------------------- WIDJET

Button(text='Generate', bd = 2, command=generate, bg = '#DCDCDC', font = ('Arial', 11, 'normal')).\
    grid(row=4, column=0, stick = 'wens', padx= 5, pady=5)

name = Entry (root, width = 15, justify=RIGHT, bd = 2, font = ('Arial', 11, 'normal'), bg = '#DCDCDC')
name.grid (row=4, column=1, stick = 'wens', padx= 5, pady=5)

Button (text = 'Clear', bd = 2, bg = '#DCDCDC', font = ('Arial', 11, 'normal'), command = lambda: name.delete(0, END)).\
    grid(row=5, column=0, stick = 'wens', padx= 5, pady=5)

Label (text='You can generate password for you needs', bg = 'grey', fg = 'white', font = ('Arial', 12, 'bold')).\
    grid (row=0,column=0, columnspan=2)

# ------------------------------------------------------------- Checkbuttons and variables

one_value = IntVar ()
two_value = IntVar ()
three_value = IntVar ()

one = Checkbutton (text = 'Letters', bg = 'grey', fg = 'black', font = ('Arial', 11, 'normal'),
                   variable = one_value,
                   offvalue = 0,
                   onvalue = 1)
one.grid (row = 1, column = 0, stick = 'w', padx= 5, pady=5)

two = Checkbutton (text = 'Symbols', bg = 'grey', fg = 'black', font = ('Arial', 11, 'normal'),
                   variable = two_value,
                   offvalue = 0,
                   onvalue = 1)
two.grid (row = 2, column = 0, stick = 'w', padx= 5, pady=5)

three = Checkbutton (text = 'Numbers', bg = 'grey', fg = 'black', font = ('Arial', 11, 'normal'),
                     variable = three_value,
                     offvalue = 0,
                     onvalue = 1)
three.grid (row = 3, column = 0, stick = 'w', padx= 5, pady=5)


Button (text = 'Select all', fg = 'black', bd = 2, bg = '#DCDCDC', font = ('Arial', 11, 'normal'), command = select_all)\
    .grid (row = 1, column = 1, stick = 'wens', padx= 5, pady=5)

Button (text = 'Deselect all', fg = 'black', bd = 2, bg = '#DCDCDC', font = ('Arial', 11, 'normal'), command = deselect_all)\
    .grid (row = 2, column = 1, stick = 'wens', padx= 5, pady=5)

# ------------------------------------------------------------- CONFIG

root.grid_columnconfigure(0, minsize=150)
root.grid_columnconfigure(1, minsize=150)
root.grid_columnconfigure(2, minsize=150)
root.grid_columnconfigure(3, minsize=150)

# ------------------------------------------------------------- IMPORTANT

root.mainloop()