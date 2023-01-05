"""I want to do password generation with with tkinter"""

from tkinter import *

root = Tk ()
root.geometry ('200x200+200+200')
root.title ('Password Generation')

btn1 = Button(text='Generate', bd = 2).grid(row=0, column=0, stick = 'wens', padx= 5, pady=5)

en = Entry (root, width = 15, justify=RIGHT, bd = 2)
en.grid (row=0, column=1, stick = 'wens', padx= 5, pady=5)

btn2 = Button (text = 'Clear', bd = 2, command = lambda: en.delete(0, END)).\
    grid(row=1, column=0, stick = 'wens', padx= 5, pady=5)

root.grid_columnconfigure(0, minsize=80)
root.grid_columnconfigure(1, minsize=80)

root.mainloop()