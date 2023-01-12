"""I want to do clock with tkinter"""

from tkinter import *
import time as t

root = Tk ()
root.title ('Clock')
root.geometry ('200x80+200+200')
root.config (bg = 'black')

l = Label (root, font = ('Arial', 30), bg = 'black', fg = 'white')
l.pack (anchor = 'center')

root.mainloop ()