"""I want to do program where I can use math formulas"""

from tkinter import *

# ------------------------ def with commands for buttons

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

def result ():
    value = entry.get()
    entry.delete(0, END)
    entry.insert(0, eval (value))

def clear ():
    entry.delete(0, END)
    entry.insert(0, '0')

# ------------------------ def with button's config

def make_button (digit):
    return Button(text= digit, bd=5, font=('Arial', 12, 'normal'), command=lambda: add_digit (digit))

def make_button_operation (operation):
    return Button(text= operation, bd=5, font=('Arial', 12, 'normal'), command=lambda: add_operation (operation))

def make_button_result (operation):
    return Button(text= operation, bd=5, font=('Arial', 12, 'normal'), command= result)

def make_button_clear (operation):
    return Button(text= operation, bd=5, font=('Arial', 12, 'normal'), command= clear)

# ------------------------ window

root = Tk ()
root.title ('Formulas')
root.geometry ('620x315+200+200')
root.config (bg = '#008B8B')

# ------------------------ labels

Label (text = 'Помощник по математическим формулам', bg = '#008B8B', font = ('Arial', 15, 'bold'), fg = 'white')\
    .grid(row = 0, column = 0, columnspan = 8, stick = 'wens', pady = 5)

Label (text = ' ', bg = '#008B8B', font = ('Arial', 12, 'bold'), fg = 'white')\
    .grid(row = 0, column = 0, stick = 'wens')

Label (text = ' ', bg = '#008B8B', font = ('Arial', 12, 'bold'), fg = 'white')\
    .grid(row = 0, column = 7, stick = 'wens')

# ------------------------ labels with description

Label (text = 'Периметр прямоугольника', bg = '#008B8B', font = ('Arial', 12, 'normal'), fg = 'white')\
    .grid(row = 2, column = 6, stick = 'wns', padx = 20)

Label (text = 'Площадь прямоугольника', bg = '#008B8B', font = ('Arial', 12, 'normal'), fg = 'white')\
    .grid(row = 3, column = 6, stick = 'wns', padx = 20)

Label (text = 'Объем параллелепипеда', bg = '#008B8B', font = ('Arial', 12, 'normal'), fg = 'white')\
    .grid(row = 4, column = 6, stick = 'wns', padx = 20)

Label (text = 'Формула пути', bg = '#008B8B', font = ('Arial', 12, 'normal'), fg = 'white')\
    .grid(row = 5, column = 6, stick = 'wns', padx = 20)

# ------------------------ labels with formulas

Label (text = '((a + b) * 2)', bg = '#008B8B', font = ('Arial', 15, 'bold'), fg = 'white')\
    .grid(row = 2, column = 5, stick = 'wns', padx = 20)

Label (text = '(a * b)', bg = '#008B8B', font = ('Arial', 15, 'bold'), fg = 'white')\
    .grid(row = 3, column = 5, stick = 'wns', padx = 20)

Label (text = '(a * b * c)', bg = '#008B8B', font = ('Arial', 15, 'bold'), fg = 'white')\
    .grid(row = 4, column = 5, stick = 'wns', padx = 20)

Label (text = '(v * t)', bg = '#008B8B', font = ('Arial', 15, 'bold'), fg = 'white')\
    .grid(row = 5, column = 5, stick = 'wns', padx = 20)

# ------------------------ entry

entry = Entry (root, bd = 3, justify=RIGHT, font=('Arial', 12, 'normal'))
entry.insert (0, '0')
entry.grid(row = 1, column = 1, columnspan = 4, stick = 'wens', padx = 3, pady = 5)

# ------------------------ digit and operation buttons

make_button (1).grid(row = 2, column = 1, stick = 'wens', pady=2, padx=4)
make_button (2).grid (row = 2, column = 2, stick = 'wens', pady=3, padx=4)
make_button (3).grid (row = 2, column = 3, stick = 'wens', pady=3, padx=4)
make_button (4).grid (row = 3, column = 1, stick = 'wens', pady=3, padx=4)
make_button (5).grid (row = 3, column = 2, stick = 'wens', pady=3, padx=4)
make_button (6).grid (row = 3, column = 3, stick = 'wens', pady=3, padx=4)
make_button (7).grid (row = 4, column = 1, stick = 'wens', pady=3, padx=4)
make_button (8).grid (row = 4, column = 2, stick = 'wens', pady=3, padx=4)
make_button (9).grid (row = 4, column = 3, stick = 'wens', pady=3, padx=4)
make_button (0).grid (row = 5, column = 1, stick = 'wens', pady=3, padx=4)

make_button_operation ('/').grid (row = 2, column = 4, stick = 'wens', pady=3, padx=4)
make_button_operation ('*').grid (row = 3, column = 4, stick = 'wens', pady=3, padx=4)
make_button_operation ('-').grid (row = 4, column = 4, stick = 'wens', pady=3, padx=4)
make_button_operation ('+').grid (row = 5, column = 4, stick = 'wens', pady=3, padx=4)

make_button_result ('=').grid (row = 5, column = 3, stick = 'wens', pady=3, padx=4)
make_button_clear ('C').grid (row = 5, column = 2, stick = 'wens', pady=3, padx=4)

# ------------------------ config for rows and columns

root.grid_columnconfigure(0, minsize = 20)
root.grid_columnconfigure(1, minsize = 50)
root.grid_columnconfigure(2, minsize = 50)
root.grid_columnconfigure(3, minsize = 50)
root.grid_columnconfigure(4, minsize = 50)
root.grid_columnconfigure(5, minsize = 50)
root.grid_columnconfigure(6, minsize = 80)

root.grid_rowconfigure(0, minsize = 30)
root.grid_rowconfigure(1, minsize = 50)
root.grid_rowconfigure(2, minsize = 50)
root.grid_rowconfigure(3, minsize = 50)
root.grid_rowconfigure(4, minsize = 50)
root.grid_rowconfigure(5, minsize = 50)

# ------------------------ the most important code ! =)

root.mainloop ()

# b'\xd0\x9e\xd1\x82\xd0\xbb\xd0\xb8\xd1\x87\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb4\xd0\xbd\xd1\x8f,
# \xd0\xb4\xd1\x80\xd1\x83\xd0\xb7\xd1\x8c\xd1\x8f!'