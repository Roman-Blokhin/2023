import pygame
import random

red = 100, 0, 0
green = 0, 250, 0
yellow = 250, 250, 0
blue = 0, 0, 100

screen_width = 300
screen_height = 400
FPS = 30

run = True

hero_x = screen_width/2
hero_y = screen_height/2
hero_width = 20
hero_height = 20

velocity = 0.05

apple_x = random.randint (5, 295)
apple_y = random.randint (5, 395)
apple_width = 15
apple_height = 15

pygame.init()
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('WarCraft')

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill(red)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and hero_x > 5:
        hero_x -= velocity

    if keys[pygame.K_RIGHT] and hero_x + hero_width < screen_width - 4:
        hero_x += velocity

    if keys[pygame.K_UP] and hero_y > 5:
        hero_y -= velocity

    if keys[pygame.K_DOWN] and hero_y + hero_height < screen_height - 4:
        hero_y += velocity

    pygame.draw.rect(win, yellow, (hero_x, hero_y, hero_width, hero_height))

    pygame.draw.rect(win, green, (apple_x, apple_y, apple_width, apple_height))

    pygame.display.update()

pygame.quit()