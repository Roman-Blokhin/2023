"""I want to do light switch with tkinter"""

from tkinter import *

root = Tk ()
root.title ('light switch')
root.geometry ('525x500+200+200')
root.config (bg = 'grey')

Label (text=' ', bg = 'grey').grid(row=0, column=0)
Label (text=' ', bg = 'grey').grid(row=1, column=3)
Label (text=' ', bg = 'grey').grid(row=1, column=0)

Button (bd = 5).grid(row=1, column=1, sticky='wens', padx=5, pady=20)
Button (bd = 5).grid(row=1, column=2, sticky='wens', padx=5, pady=20)

root.grid_columnconfigure(0, minsize=65)
root.grid_columnconfigure(1, minsize=200)
root.grid_columnconfigure(2, minsize=200)

root.grid_rowconfigure(0, minsize=70)
root.grid_rowconfigure(1, minsize=360)

root.mainloop ()