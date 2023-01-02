"""I want to make program to desktop that can open web links for my convenience"""

from tkinter import *
import webbrowser as wb

def open_git(e=None):
    wb.open('https://github.com/Roman-Blokhin')

def open_youtube(e=None):
    wb.open('https://www.youtube.com/')

def open_codewars(e=None):
    wb.open('https://www.codewars.com/')

def open_robochat(e=None):
    wb.open('https://robochat.io/')

def open_color(e=None):
    wb.open('https://colorscheme.ru/html-colors.html')

def open_ico(e=None):
    wb.open('https://icon-icons.com/ru/')

root = Tk ()
root.geometry ('300x70+10+700')
root.title ('links')

Button (text='GIT', bd=3, bg='black', font=('Arial', 10, 'normal'), fg = 'white', command=open_git).\
    grid(row=0, column=0, stick='wens')

Button (text='CodeWars', bd=3, bg='black', font=('Arial', 10, 'normal'), fg = 'white', command=open_codewars).\
    grid(row=1, column=0, stick='wens')

Button (text='Robo', bd=3, bg='black', font=('Arial', 10, 'normal'), fg = 'white', command=open_robochat).\
    grid(row=0, column=1, stick='wens')

Button (text='YouTube', bd=3, bg='black', font=('Arial', 10, 'normal'), fg = 'white', command=open_youtube).\
    grid(row=1, column=1, stick='wens')

Button (text='Color', bd=3, bg='black', font=('Arial', 10, 'normal'), fg = 'white', command=open_color).\
    grid(row=0, column=2, stick='wens')

Button (text='ICO', bd=3, bg='black', font=('Arial', 10, 'normal'), fg = 'white', command=open_ico).\
    grid(row=1, column=2, stick='we')

root.grid_columnconfigure(0, minsize=80)
root.grid_columnconfigure(1, minsize=80)
root.grid_columnconfigure(2, minsize=80)

root.mainloop ()