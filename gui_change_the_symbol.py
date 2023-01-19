"""I want to do program where you can put the text and change symbol that you want"""

from tkinter import *


# -------------------------------------------------- DEF

def change():
    a = entry_symbol.get()
    b = entry_change.get()
    c = entry_text.get(1.0, END)
    d = c.replace(a, b)
    e = len(c) - 1
    # value_d = result.get(1.0, END)
    result.delete(1.0, END)
    result.insert(1.0, d)
    print('1. ', a)
    print('2. ', b)
    print('3. ', c)
    print('4. ', d)
    Label (text=e, bg='#008B8B', font=('Arial', 12, 'bold'), fg='black').grid(row=5, column=2, sticky='e')


# -------------------------------------------------- WINDOW

root = Tk()
root.title('Change the symbol')
root.geometry('550x350+200+200')
root.config(bg='#008B8B')

# -------------------------------------------------- WIDJETS

Label(text='Программа для удаления ненужных символов из текста', bg='#008B8B', font=('Arial', 12, 'bold'), fg='white') \
    .grid(row=0, column=0, columnspan=3, sticky='w')
# -----------------------
Label(text='Символ для удаления', bg='#008B8B', font=('Arial', 10, 'bold')).grid(row=1, column=0, sticky='w')

entry_symbol = Entry(root, width=5, bd=3, justify=RIGHT, font=('Arial', 12, 'bold'))
entry_symbol.grid(row=1, column=1, padx=5, pady=5, stick='w')
# -----------------------
Label(text='Символ, который нужно проставить', bg='#008B8B', font=('Arial', 10, 'bold')) \
    .grid(row=2, column=0, sticky='w')

entry_change = Entry(root, width=5, bd=3, justify=RIGHT, font=('Arial', 12, 'bold'))
entry_change.grid(row=2, column=1, padx=5, pady=5, stick='w')
# -----------------------
Label(text='Ваш текст:', bg='#008B8B', font=('Arial', 12, 'bold'), fg='white').grid(row=3, column=0, sticky='w')

entry_text = Text(root, wrap=WORD, width=25, height=5, bd=3, font=('Arial', 12, 'bold'))
entry_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5, stick='w')
# -----------------------
Label(text='Результат:', bg='#008B8B', font=('Arial', 12, 'bold'), fg='white').grid(row=3, column=1, sticky='w')

result = Text(root, wrap=WORD, width=25, height=5, bd=3, font=('Arial', 12, 'bold'))
result.grid(row=4, column=1, columnspan=2, padx=5, pady=5, stick='w')
# -----------------------
start = Button(text='Внести изменения', font=('Arial', 12), command=change)
start.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky='w')
# -----------------------
Label(text='Символов в тексте: ', bg='#008B8B', font=('Arial', 12, 'bold'), fg='white').grid(row=5, column=1, sticky='w')

# -------------------------------------------------- ROW'S AND COLUMN'S CONFIG

root.grid_columnconfigure(0, minsize=2)
root.grid_columnconfigure(1, minsize=2)

root.grid_rowconfigure(0, minsize=20)
root.grid_rowconfigure(1, minsize=20)
root.grid_rowconfigure(2, minsize=20)
root.grid_rowconfigure(3, minsize=20)
root.grid_rowconfigure(4, minsize=20)

# -------------------------------------------------- IMPORTANT

root.mainloop()
