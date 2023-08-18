import pygame as pg
import random

WIDTH = 400 # ширина экрана
HEIGHT = 500 # высота экрана
FPS = 30 # кол-во кадров в секунду

# создаем игру и окно
pg.init()
pg.mixer.init() # для звука
screen = pg.display.set_mode((WIDTH, HEIGHT)) # создаем экран
pg.display.set_caption('WarCraft') # title
clock = pg.time.Clock() # игра работает с заданной частотой кадров