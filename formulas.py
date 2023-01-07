"""I want to do program where I can use math formulas"""

from tkinter import *

root = Tk ()
root.title ('Formulas')
root.geometry ('400x400+200+200')
root.config (bg = 'grey')

Label (text = 'Помощник по математическим формулам', bg = 'grey', font = ('Arial', 12, 'normal'), fg = 'white')\
    .grid(row = 0, column = 0, columnspan = 6, stick = 'wens')

root.grid_columnconfigure(0, minsize = 50)
root.grid_columnconfigure(1, minsize = 50)
root.grid_columnconfigure(2, minsize = 50)
root.grid_columnconfigure(3, minsize = 50)
root.grid_columnconfigure(4, minsize = 50)
root.grid_columnconfigure(5, minsize = 50)

root.mainloop ()