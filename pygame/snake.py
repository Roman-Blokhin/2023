import pygame
import random
import time
pygame.init()

red = 100, 0, 0
green = 0, 250, 0
yellow = 250, 250, 0
blue = 0, 0, 100
black = 0, 0, 0
white = 255, 255, 255

screen_width = 300
screen_height = 400
FPS = 7

run = True

hero_x = screen_width/2
hero_y = screen_height/2
hero_width = 20
hero_height = 20

x1_change = 0
y1_change = 0

apple_x = random.randint (5, 290)
apple_y = random.randint (5, 390)
apple_width = 15
apple_height = 15

second_win = pygame.font.SysFont(None, 50) # создали сообщение, которое высветится поверх экрана

def message (msg, color): # создаем функцию для появления сообщения по окончанию игры
    mesg = second_win.render(msg, True, color) # создаем слой
    win.blit(mesg, [50, 200]) # отрисовываем сообщение на основной поверхности

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('WarCraft')
clock = pygame.time.Clock()

while run:
    win.fill(red)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x1_change = -10
            y1_change = 0
        if keys[pygame.K_RIGHT]:
            x1_change = +10
            y1_change = 0
        if keys[pygame.K_UP]:
            y1_change = -10
            x1_change = 0
        if keys[pygame.K_DOWN]:
            y1_change = +10
            x1_change = 0

    if hero_x + hero_width >= screen_width-10 or hero_x <= 10 or \
            hero_y + hero_height >= screen_height-10 or hero_y <= 10:
        print('GAME OVER')
        run = False

    hero_x += x1_change
    hero_y += y1_change

    pygame.draw.rect(win, yellow, (hero_x, hero_y, hero_width, hero_height))
    pygame.draw.rect(win, green, (apple_x, apple_y, apple_width, apple_height))

    clock.tick(FPS)
    pygame.display.update()

win.fill(white) # установил слой заливки поверх экрана цикла
message('GAME OVER', red)
pygame.display.update()
time.sleep(2)

pygame.quit()