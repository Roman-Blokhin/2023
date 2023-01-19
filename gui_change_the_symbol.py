"""I want to do program where you can put the text and change symbol that you want"""

from tkinter import *

root = Tk ()
root.title ('Change the symbol')
root.geometry ('350x350+200+200')
root.config (bg = '#008B8B')

entry_symbol = Entry (root)
entry_symbol.grid (row=0, column=0, padx=5, pady=5)

entry_change = Entry (root)
entry_change.grid (row=1, column=0, padx=5, pady=5)

entry_text = Entry (root)
entry_text.grid (row=3, column=0, padx=5, pady=5)

result = Entry (root)
result.grid (row=5, column=0, padx=5, pady=5)

start = Button (text='Start')
start.grid (row=4, column=0, padx=5, pady=5)

root.mainloop ()