"""I want to do some pop-up windows: information, warning and error"""

from tkinter import *
import tkinter.messagebox as mb

def information ():
    text = 'This is information window'
    mb.showinfo ('Info', text)

def warning ():
    text = 'Warning! Don\'t make mistake!'
    mb.showwarning('Warning', text)

root = Tk ()
root.geometry ('507x117+200+200')
root.title ('Windows')
root.config (bg = 'grey')

Button (text = 'Information', font = ('Arial', 15, 'italic'), bd = 5, bg = 'pink', fg = 'white', command=information).\
    grid (row= 0, column = 0, stick = 'wens', padx = 5, pady = 5)

Button (text = 'Warning', font = ('Arial', 15, 'normal'), bd = 5, command=warning).\
    grid (row= 0, column = 2, stick = 'wens', padx = 5, pady = 5)

Button (text = 'Error', font = ('Arial', 15, 'bold'), bd = 5, bg = '#87CEEB').\
    grid (row= 1, column = 1, stick = 'wens', padx = 5, pady = 5)

root.grid_columnconfigure (0, minsize=170)
root.grid_columnconfigure (1, minsize=170)
root.grid_columnconfigure (2, minsize=170)

root.rowconfigure (1, minsize=30)
root.rowconfigure (1, minsize=30)

root.mainloop()