import pygame as pg
import random


# 1 задаем переменные: размеры и цвета
WIDTH = 400 # ширина экрана
HEIGHT = 500 # высота экрана
FPS = 30 # кол-во кадров в секунду

RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
WHITE = 255, 255, 255
BLACK = 0, 0, 0


# 2 создаем игру и окно
pg.init()
pg.mixer.init() # для звука
pg.display.set_caption('WarCraft') # title
screen = pg.display.set_mode((WIDTH, HEIGHT)) # создаем экран
clock = pg.time.Clock() # игра работает с заданной частотой кадров

# рендеринг - отрисовка
screen.fill(RED) # экран красный для компьютера - обр. сторона доски - заполнять
pg.display.flip() # поворачиваем обратную сторону доски к пользователю - сальто


# 3 Цикл игры
running = True
a = 100000
while running:
    # Ввод процесса (события)
    # Обновление
    # Визуализация (сборка)
    a -= 1
    print(a)
    if a == 0:
        running = False

