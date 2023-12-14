from tkinter import *
from tkinter import messagebox  # 13. чтобы получать всплывающие окна


# ----------------------------- ФУНКЦИИ -----------------------------

# 11 подключаем функцию к параметрам текстового поля, чтобы можно было менять
def change_color(theme):
    text_fild['bg'] = view_color[theme]['color_bg']
    text_fild['fg'] = view_color[theme]['color_fg']
    text_fild['insertbackground'] = view_color[theme]['color_cursor']
    text_fild['selectbackground'] = view_color[theme]['color_select_bg']


# 12.1 подключаем шрифты к меню
def change_font(fontss):
    text_fild['font'] = fonts[fontss]['font']


# 13.1 пишем команду для выхода
def notepad_exit():
    answer = messagebox.askokcancel('Выход', 'Выйти из программы?')
    if answer:
        root.destroy()


# ----------------------------- ОКНО -----------------------------

# 1. создали основу для программы, окно
root = Tk()
root.title('Блокнот')
root.geometry('650x450+200+200')
root.iconbitmap(default='logo.ico')

# ----------------------------- 10. СЛОВАРЬ С ЦВЕТОВЫМИ ТЕМАМИ -----------------------------

view_color = {  # прописываем словари с цветами по каждым параметрам в текстовом поле
    'dark': {
        'color_bg': 'black', 'color_fg': 'lime', 'color_cursor': 'brown', 'color_select_bg': '#8D917A'
    },
    'light': {
        'color_bg': 'white', 'color_fg': 'black', 'color_cursor': 'red', 'color_select_bg': 'blue'
    },
    'grey': {
        'color_bg': 'darkgrey', 'color_fg': 'white', 'color_cursor': 'black', 'color_select_bg': 'pink'
    }
}

# ----------------------------- 12. Шрифты -----------------------------

fonts = {
    'Arial': {
        'font': ('Arial', 14, 'normal')
    },
    'Comic Sans MS': {
        'font': ('Comic Sans MS', 14, 'normal')
    },
    'Times New Roman': {
        'font': ('Times New Roman', 14, 'normal')
    },

}

# ----------------------------- МЕНЮ -----------------------------

main_menu = Menu(root)  # 4. создаем главное меню

# 6.1 меню - Файл
file_menu = Menu(main_menu, tearoff=0)  # tearoff=0 - убирает ненужную пунктирную линию из меню
file_menu.add_command(label='Открыть')  # добавляем слоты для команд
file_menu.add_command(label='Сохранить')
file_menu.add_separator()  # добавили полоску разделитель
file_menu.add_command(label='Выход', command=notepad_exit)
root.config(menu=file_menu)  # устанавливаем меню в наше окно

# 8.1 меню - Вид
view_menu = Menu(main_menu, tearoff=0)

view_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label='Темная', command=lambda: change_color('dark'))  # 11.1 прописываем команду
view_menu_sub.add_command(label='Светлая', command=lambda: change_color('light'))
view_menu_sub.add_command(label='Серая', command=lambda: change_color('grey'))
view_menu.add_cascade(menu=view_menu_sub, label='Тема')

font_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub.add_command(label='Arial', command=lambda: change_font('Arial'))
font_menu_sub.add_command(label='Comic Sans MS', command=lambda: change_font('Comic Sans MS'))
font_menu_sub.add_command(label='Times New Roman', command=lambda: change_font('Times New Roman'))
view_menu.add_cascade(menu=font_menu_sub, label='Шрифт')

root.config(menu=view_menu)

# 9.1 меню - Информация
info_menu = Menu(main_menu, tearoff=0)
info_menu.add_command(label='О нас')
root.config(menu=info_menu)

main_menu.add_cascade(label='Файл', menu=file_menu)  # 7. выводим каскад меню на экран
main_menu.add_cascade(label='Вид', menu=view_menu)  # 8. выводим каскад меню на экран
main_menu.add_cascade(label='Инфо', menu=info_menu)  # 9. выводим каскад меню на экран

root.config(menu=main_menu)  # 5. устанавливаем меню в наше окно(всегда в конце)

# ----------------------------- ФРЕЙМ(КОНТЕЙНЕР) -----------------------------

f_text = Frame(root)  # 2. создали контейнер для текстового поля
f_text.pack(fill=BOTH,  # растягивание по сторонам х и у
            expand=1)  # виджет заполняющий все пространство экрана

# ----------------------------- ТЕКСТОВОЕ ПОЛЕ -----------------------------

text_fild = Text(f_text,
                 bg='black',
                 fg='lime',
                 padx=10,
                 pady=10,
                 wrap=WORD,  # ПЕРЕНОС ТЕКСТА ПО СЛОВАМ
                 insertbackground='brown',  # ДОБАВЛЯЕМ КУРСОР, УКАЗЫВАЕМ ЦВЕТ
                 selectbackground='#8D917A',  # ЦВЕТ ВЫДЕЛЕННОГО ТЕКСТА
                 spacing3=10,  # ДОБАВИЛИ ОТСТУПЫ У АБЗАЦЕВ
                 width=30,  # ШИРИНА СКРОЛЛБАРА
                 font='Arial 14 normal'
                 )
text_fild.pack(fill=BOTH, expand=1, side=LEFT)  # 3. side=LEFT - выравнивание по левой стороне контейнера

# ----------------------------- пАНЕЛЬ ПРОКРУТКИ -----------------------------

# 4. добавляем панель прокрутки текста вниз по оси Y
scroll = Scrollbar(f_text, command=text_fild.yview)  # встроенный виджет для прокрутки по вертикали
scroll.pack(fill=Y, side=LEFT)
text_fild.config(yscrollcommand=scroll.set)

# ----------------------------- ВАЖНОЕ -----------------------------

root.mainloop()
