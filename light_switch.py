"""I want to do light switch with tkinter"""

from tkinter import *

root = Tk ()
root.title ('light switch')
root.geometry ('525x500+200+200')
root.config (bg = 'grey')

Button (bd = 5).grid(row=0, column=1, sticky='wens', padx=5, pady=20)
Button (bd = 5).grid(row=0, column=2, sticky='wens', padx=5, pady=20)

root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=200)
root.grid_columnconfigure(2, minsize=200)

root.grid_rowconfigure(0, minsize=400)
root.grid_rowconfigure(0, minsize=400)

root.mainloop ()