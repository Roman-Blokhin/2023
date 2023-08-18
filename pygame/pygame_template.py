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


# 3 Цикл игры
running = True
while running:
    # рендеринг - отрисовка
    screen.fill(RED) # экран красный для компьютера - обр. сторона доски - заполнять
    pg.display.flip() # поворачиваем обратную сторону доски к пользователю - сальто

    clock.tick(FPS) # держим цикл на заданной правильной скорости

    # Ввод процесса (события)
    for event in pg.event.get(): # если полученное событие:
        if event.type == pg.QUIT: # подключаем крестик для выхода
            running = False

    # Обновление
    # Визуализация (сборка)


pg.quit() # обязательный выход

