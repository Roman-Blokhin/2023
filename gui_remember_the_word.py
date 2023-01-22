from tkinter import *
import random as r
import os
from time import sleep

quantity = 3

# -------------------------------- Def

def random_word ():
    chars = ('abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
    word = r.sample (chars, quantity)
    word = ''.join (word)

    value = entry_1.get ()
    if value [3:] in chars:
        value = value [3:]
    entry_1.delete(0, END)
    entry_1.insert (0, value + word)

    print ('entry_1: ' + word)
    # entry_1.delete(0, END)

    # TODO: СДЕЛАТЬ ТАК, ЧТОБЫ ПОЛЕ ВВОДА 1 ОЧИЩАЛОСЬ

def compare_entries ():
    score_level = 0
    value_1 = entry_2.get ()
    value_2 = entry_1.get ()
    if value_1 == value_2:
        score = 0
        Label (text = 'Good boy!', bg = 'pink').grid (row = 6, column = 0)
        score += 1
        Label (text = score, bg = 'pink', bd = 3).grid (row=2, column=2, sticky='w')
        print ('entry_2: ' + value_1)
        print (score)
        if value_1 != value_2:
            Label(text='   Omg..   ', bg='pink').grid (row = 6, column = 0)
            score -= 1
            print ('entry_2: ' + value_1)
            print(score)

    #TODO: СДЕЛАТЬ ТАК, ЧТОБЫ ОЧКИ МЕНЯЛИСЬ, А ПОТОМ И УРОВЕНЬ

def clear_entries():
    entry_1.get ()
    entry_2.get ()
    entry_1.delete(0, END)
    entry_2.delete(0, END)

# -------------------------------- Window configures

root = Tk ()
root.title ('Game: Remember the word')
root.geometry ('350x350+200+200')
root.config (bg = 'pink')

# -------------------------------- Labels, Entries, Buttons

Label (text = 'Запомни слово', bg = 'pink', bd = 3).grid (row=0, column=0, columnspan=5)
Button (text = 'Начать', bd = 3, command = random_word).grid (row=1, column=0, stick = 'wens', padx = 5, pady = 5)

entry_1 = Entry (root, justify = RIGHT, bd = 3)
entry_1.grid (row = 2, column = 0, stick = 'wens', padx = 5, pady = 5)

Label (text = 'Введите слово: ', bg = 'pink', bd = 3).grid (row=3, column=0)

entry_2 = Entry (root, justify = RIGHT, bd = 3)
entry_2.grid (row = 4, column = 0, stick = 'wens', padx = 5, pady = 5)

Button (text = 'Сравнить', bd = 3, command = compare_entries).grid (row=5, column=0, stick = 'wens', padx = 5, pady = 5)

Label (text = 'Level: ', bg = 'pink', bd = 3).grid (row=1, column=1)
Label (text = 'Score: ', bg = 'pink', bd = 3).grid (row=2, column=1)

Button (text = 'Clear', command = clear_entries).grid (row = 3, column = 1)

entry_3 = Entry (root, justify = RIGHT, bd = 3)
entry_3.insert (0, 0)
entry_3.grid (row = 1, column = 2, padx = 5, pady = 5)

# -------------------------------- Other configures

root.grid_columnconfigure(0, minsize = 70)
root.grid_columnconfigure(1, minsize = 70)
root.grid_columnconfigure(2, minsize = 70)
root.grid_columnconfigure(3, minsize = 70)

root.grid_rowconfigure(0, minsize = 30)
root.grid_rowconfigure(1, minsize = 30)
root.grid_rowconfigure(2, minsize = 30)
root.grid_rowconfigure(3, minsize = 30)
root.grid_rowconfigure(4, minsize = 30)
root.grid_rowconfigure(5, minsize = 30)
root.grid_rowconfigure(6, minsize = 30)

# -------------------------------- The most important config =)

root.mainloop ()