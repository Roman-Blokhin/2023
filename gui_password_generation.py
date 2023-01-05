"""I want to do password generation with with tkinter"""

from tkinter import *

root = Tk ()
root.geometry ('200x200+200+200')
root.title ('Password Generation')

btn1 = Button(text='Generate').grid(row=0, column=0)

root.mainloop()