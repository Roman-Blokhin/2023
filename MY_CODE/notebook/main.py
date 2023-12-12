from tkinter import *

# 1. создали основу для программы, окно

root = Tk()
root.title('Блокнот')
root.geometry('650x450+200+200')
root.iconbitmap(default='logo.ico')

f_text = Frame(root)  # 2. создали контейнер для текстового поля
f_text.pack(fill=BOTH, expand=1)  # 3. fill=BOTH - растяг. по сторонам х и у, expand=1 - виджет заполн. все простр.

text_fild = Text(f_text, bg='black', fg='lime')
text_fild.pack(fill=BOTH, expand=1, side=LEFT)  # 3. side=LEFT - выравнивание по левой стороне контейнера

root.mainloop()
