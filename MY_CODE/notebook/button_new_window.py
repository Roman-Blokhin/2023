from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import random as r

# ----------------------------- НАША ФУНКЦИЯ ДЛЯ КНОПКИ - НОВОЕ ОКНО -----------------------------
def new_window():
    # ----------------------------- ПЕРЕМЕННЫЕ -----------------------------
    num_1 = r.randint(100, 300)  # переменные для определения координат в создании нового окна
    num_2 = r.randint(100, 300)

    # ----------------------------- ФУНКЦИИ -----------------------------
    def change_color(theme):
        text_fild['bg'] = view_color[theme]['color_bg']
        text_fild['fg'] = view_color[theme]['color_fg']
        text_fild['insertbackground'] = view_color[theme]['color_cursor']
        text_fild['selectbackground'] = view_color[theme]['color_select_bg']

    def change_font(fontss):
        text_fild['font'] = fonts[fontss]['font']

    def notepad_exit():
        answer = messagebox.askokcancel('Выход', 'Выйти из программы?')
        if answer:
            root.destroy()

    def open_file():
        filepath = filedialog.askopenfilename(
            title='Выбор файла', filetypes=(('Текстовый документ', '*.txt'), ('Все файлы', '*.*')))
        if filepath:
            text_fild.delete('1.0', END)
            text_fild.insert('1.0', open(filepath, encoding='utf-8').read())

    def save_file():
        filepath = filedialog.asksaveasfilename(
            title='Сохранить файл', filetypes=(('Текстовый документ', '*.txt'), ('Все файлы', '*.*')))
        f = open(filepath, 'w', encoding='utf-8')
        text = text_fild.get('1.0', END)
        f.write(text)
        f.close()

    # ----------------------------- ОКНО -----------------------------

    root = Tk()
    root.title('Блокнот')
    root.geometry (f'650x450+{num_1}+{num_2}')
    root.iconbitmap(default='logo.ico')

    root.protocol('WM_DELETE_WINDOW', notepad_exit)

    # ----------------------------- 10. СЛОВАРЬ С ЦВЕТОВЫМИ ТЕМАМИ -----------------------------

    view_color = {
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

    main_menu = Menu(root)

    file_menu = Menu(main_menu, tearoff=0)
    file_menu.add_command(label='Открыть', command=open_file)
    file_menu.add_command(label='Новое окно', command=new_window)
    file_menu.add_command(label='Сохранить', command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label='Выход', command=notepad_exit)
    root.config(menu=file_menu)

    view_menu = Menu(main_menu, tearoff=0)

    view_menu_sub = Menu(view_menu, tearoff=0)
    view_menu_sub.add_command(label='Темная', command=lambda: change_color('dark'))
    view_menu_sub.add_command(label='Светлая', command=lambda: change_color('light'))
    view_menu_sub.add_command(label='Серая', command=lambda: change_color('grey'))
    view_menu.add_cascade(menu=view_menu_sub, label='Тема')

    font_menu_sub = Menu(view_menu, tearoff=0)
    font_menu_sub.add_command(label='Arial', command=lambda: change_font('Arial'))
    font_menu_sub.add_command(label='Comic Sans MS', command=lambda: change_font('Comic Sans MS'))
    font_menu_sub.add_command(label='Times New Roman', command=lambda: change_font('Times New Roman'))
    view_menu.add_cascade(menu=font_menu_sub, label='Шрифт')

    root.config(menu=view_menu)

    info_menu = Menu(main_menu, tearoff=0)
    info_menu.add_command(label='О нас')
    root.config(menu=info_menu)

    main_menu.add_cascade(label='Файл', menu=file_menu)
    main_menu.add_cascade(label='Вид', menu=view_menu)
    main_menu.add_cascade(label='Инфо', menu=info_menu)

    root.config(menu=main_menu)

    # ----------------------------- ФРЕЙМ(КОНТЕЙНЕР) -----------------------------

    f_text = Frame(root)
    f_text.pack(fill=BOTH,
                expand=1)

    # ----------------------------- ТЕКСТОВОЕ ПОЛЕ -----------------------------

    text_fild = Text(f_text,
                     bg='black',
                     fg='lime',
                     padx=10,
                     pady=10,
                     wrap=WORD,
                     insertbackground='brown',
                     selectbackground='#8D917A',
                     spacing3=10,
                     width=30,
                     font='Arial 14 normal'
                     )
    text_fild.pack(fill=BOTH, expand=1, side=LEFT)

    # ----------------------------- пАНЕЛЬ ПРОКРУТКИ -----------------------------

    scroll = Scrollbar(f_text, command=text_fild.yview)
    scroll.pack(fill=Y, side=LEFT)
    text_fild.config(yscrollcommand=scroll.set)

    # ----------------------------- ВАЖНОЕ -----------------------------

    root.mainloop()
