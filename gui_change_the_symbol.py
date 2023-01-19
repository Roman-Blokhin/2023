"""I want to do program where you can put the text and change symbol that you want"""

from tkinter import *


# -------------------------------------------------- DEF

def change():
    a = entry_symbol.get()
    b = entry_change.get()
    c = entry_text.get(1.0, END)
    d = c.replace(a, b)
    value_d = result.get(1.0, END)
    result.delete(1.0, END)
    result.insert(1.0, d)
    print('1. ', a)
    print('2. ', b)
    print('3. ', c)
    print('4. ', d)


# -------------------------------------------------- WINDOW

root = Tk()
root.title('Change the symbol')
root.geometry('350x350+200+200')
root.config(bg='#008B8B')

# -------------------------------------------------- WIDJETS

entry_symbol = Entry(root)
entry_symbol.grid(row=0, column=0, padx=5, pady=5, stick='wens')

entry_change = Entry(root)
entry_change.grid(row=1, column=0, padx=5, pady=5, stick='wens')

entry_text = Text(root, wrap=WORD, width=20, height=5)
entry_text.grid(row=3, column=0, padx=5, pady=5)

result = Text(root, wrap=WORD, width=20, height=5)
result.grid(row=5, column=0, padx=5, pady=5)

start = Button(text='Внести изменения', command=change)
start.grid(row=4, column=0, padx=5, pady=5)

Label(text='Вставьте текст', bg='#008B8B').grid(row=2, column=0, sticky='w')

# -------------------------------------------------- ROW'S AND COLUMN'S CONFIG

root.grid_columnconfigure(0, minsize=10)
root.grid_columnconfigure(1, minsize=10)

root.grid_rowconfigure(0, minsize=20)
root.grid_rowconfigure(1, minsize=20)
root.grid_rowconfigure(2, minsize=20)
root.grid_rowconfigure(3, minsize=20)
root.grid_rowconfigure(4, minsize=20)

# -------------------------------------------------- IMPORTANT

root.mainloop()
