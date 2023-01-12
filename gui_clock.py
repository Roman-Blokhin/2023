"""I want to do clock with tkinter"""

from tkinter import *
import time as t

#функция отображения наших часов
def time ():
    clock = t.strftime ('%H:%M:%S %p')
    l.config (text = clock)
    l.after (1000, time) # устанавливаем параметры изменения нашего времени, 1000мс = 1с
    print (clock)

root = Tk ()
root.title ('Clock')
root.geometry ('300x80+200+200')
root.config (bg = 'black')

# размещаем параметры текста на окне
l = Label (root, font = ('Arial', 30), bg = 'black', fg = 'white')
l.pack (anchor = 'center')

# запускаем нашу функцию
time()

root.mainloop ()