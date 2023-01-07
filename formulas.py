"""I want to do program where I can use math formulas"""

from tkinter import *

def add_digit (digit):
    value = entry.get () + str (digit)
    if value [:1] == '0':
        value = value [1:]
    entry.delete (0, END)
    entry.insert (0, value)

def add_operation (operation):
    value = entry.get ()
    if value [-1] in '+-/*':
        value = value [:1]
    entry.delete (0, END)
    entry.insert(0, value + operation)

def make_button (digit):
    return Button(text= digit, bd=5, font=('Arial', 12, 'normal'), command=lambda: add_digit (digit))

def make_button_operation (operation):
    return Button(text= operation, bd=5, font=('Arial', 12, 'normal'), command=lambda: add_operation (operation))

root = Tk ()
root.title ('Formulas')
root.geometry ('500x300+200+200')
root.config (bg = 'grey')

Label (text = 'Помощник по математическим формулам', bg = 'grey', font = ('Arial', 12, 'normal'), fg = 'white')\
    .grid(row = 0, column = 0, columnspan = 6, stick = 'wens')

entry = Entry (root, bd = 5, justify=RIGHT, font=('Arial', 12, 'normal'))
entry.insert (0, 0)
entry.grid(row = 1, column = 0, columnspan = 4, stick = 'wens', padx = 5, pady = 5)

make_button (1).grid(row = 2, column = 0, stick = 'wens', pady=3, padx=5)
make_button (2).grid (row = 2, column = 1, stick = 'wens', pady=3, padx=5)
make_button (3).grid (row = 2, column = 2, stick = 'wens', pady=3, padx=5)
make_button (4).grid (row = 3, column = 0, stick = 'wens', pady=3, padx=5)
make_button (5).grid (row = 3, column = 1, stick = 'wens', pady=3, padx=5)
make_button (6).grid (row = 3, column = 2, stick = 'wens', pady=3, padx=5)
make_button (7).grid (row = 4, column = 0, stick = 'wens', pady=3, padx=5)
make_button (8).grid (row = 4, column = 1, stick = 'wens', pady=3, padx=5)
make_button (9).grid (row = 4, column = 2, stick = 'wens', pady=3, padx=5)
make_button (0).grid (row = 5, column = 0, stick = 'wens', pady=3, padx=5)

make_button_operation ('/').grid (row = 2, column = 3, stick = 'wens', pady=3, padx=5)
make_button_operation ('*').grid (row = 3, column = 3, stick = 'wens', pady=3, padx=5)
make_button_operation ('-').grid (row = 4, column = 3, stick = 'wens', pady=3, padx=5)
make_button_operation ('+').grid (row = 5, column = 3, stick = 'wens', pady=3, padx=5)

make_button ('C').grid (row = 5, column = 1, stick = 'wens', pady=3, padx=5)

make_button ('=').grid (row = 5, column = 2, stick = 'wens', pady=3, padx=5)

root.grid_columnconfigure(0, minsize = 50)
root.grid_columnconfigure(1, minsize = 50)
root.grid_columnconfigure(2, minsize = 50)
root.grid_columnconfigure(3, minsize = 50)
root.grid_columnconfigure(4, minsize = 50)
root.grid_columnconfigure(5, minsize = 50)

root.grid_rowconfigure(0, minsize = 10)
root.grid_rowconfigure(1, minsize = 30)
root.grid_rowconfigure(2, minsize = 30)
root.grid_rowconfigure(3, minsize = 30)
root.grid_rowconfigure(4, minsize = 30)
root.grid_rowconfigure(5, minsize = 30)

root.mainloop ()