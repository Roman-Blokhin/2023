"""I want to make program to desktop that can open web links for my convenience"""

from tkinter import *
import webbrowser as wb

def open_git():
    wb.open('https://github.com/Roman-Blokhin')

def open_youtube():
    wb.open('https://www.youtube.com/')

def open_codewars():
    wb.open('https://www.codewars.com/')

def open_robochat():
    wb.open('https://robochat.io/')

def open_color():
    wb.open('https://colorscheme.ru/html-colors.html')

def open_ico():
    wb.open('https://icon-icons.com/ru/')

root = Tk ()
root.geometry ('238x58+10+700')
root.title ('links')

Button (text='GIT', bd=3, bg='black', font=('Arial', 10, 'bold'), fg = 'white', command=open_git).\
    grid(row=0, column=0, stick='wens')

Button (text='CodeWars', bd=3, bg='#FA8072', font=('Arial', 10, 'bold'), fg = 'black', command=open_codewars).\
    grid(row=1, column=0, stick='wens')

Button (text='Robo', bd=3, bg='#FF8C00', font=('Arial', 10, 'bold'), fg = 'black', command=open_robochat).\
    grid(row=0, column=1, stick='wens')

Button (text='YouTube', bd=3, bg='red', font=('Arial', 10, 'bold'), fg = 'white', command=open_youtube).\
    grid(row=1, column=1, stick='wens')

Button (text='Color', bd=3, bg='grey', font=('Arial', 10, 'bold'), fg = 'white', command=open_color).\
    grid(row=0, column=2, stick='wens')

Button (text='ICO', bd=3, bg='#B0E0E6', font=('Arial', 10, 'bold'), fg = 'black', command=open_ico).\
    grid(row=1, column=2, stick='we')

root.grid_columnconfigure(0, minsize=80)
root.grid_columnconfigure(1, minsize=80)
root.grid_columnconfigure(2, minsize=80)

root.mainloop ()