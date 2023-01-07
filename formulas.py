"""I want to do program where I can use math formulas"""

from tkinter import *

root = Tk ()
root.title ('Formulas')
root.geometry ('400x400+200+200')
root.config (bg = 'grey')

Label (text = 'Помощник по математическим формулам', bg = 'grey', font = ('Arial', 12, 'normal'), fg = 'white')\
    .grid(row = 0, column = 0, columnspan = 6, stick = 'wens')

entry = Entry (root, bd = 5, justify=RIGHT)
entry.grid(row = 1, column = 0, columnspan = 4, stick = 'wens', padx = 5, pady = 5)

Button (text='1', bd = 5, font = ('Arial', 10, 'normal')).grid (row = 2, column = 0, stick = 'wens', pady=3, padx=5)
Button (text='2', bd = 5, font = ('Arial', 10, 'normal')).grid (row = 2, column = 1, stick = 'wens', pady=3, padx=5)
Button (text='3', bd = 5, font = ('Arial', 10, 'normal')).grid (row = 2, column = 2, stick = 'wens', pady=3, padx=5)
Button (text='4', bd = 5, font = ('Arial', 10, 'normal')).grid (row = 3, column = 0, stick = 'wens', pady=3, padx=5)
Button (text='5', bd = 5, font = ('Arial', 10, 'normal')).grid (row = 3, column = 1, stick = 'wens', pady=3, padx=5)
Button (text='6', bd = 5, font = ('Arial', 10, 'normal')).grid (row = 3, column = 2, stick = 'wens', pady=3, padx=5)
Button (text='7', bd = 5, font = ('Arial', 10, 'normal')).grid (row = 4, column = 0, stick = 'wens', pady=3, padx=5)
Button (text='8', bd = 5, font = ('Arial', 10, 'normal')).grid (row = 4, column = 1, stick = 'wens', pady=3, padx=5)
Button (text='9', bd = 5, font = ('Arial', 10, 'normal')).grid (row = 4, column = 2, stick = 'wens', pady=3, padx=5)
Button (text='0', bd = 5, font = ('Arial', 10, 'normal')).grid (row = 5, column = 0, stick = 'wens', pady=3, padx=5)

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