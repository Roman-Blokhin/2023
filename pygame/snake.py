import pygame
import random

red = 100, 0, 0
green = 0, 250, 0
yellow = 250, 250, 0
blue = 0, 0, 100

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

apple_x = random.randint (5, 295)
apple_y = random.randint (5, 395)
apple_width = 15
apple_height = 15

score = 0

pygame.init()
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

        if hero_x >= screen_width or hero_x <= 0 or hero_y >= screen_height or hero_y <= 0:
            print('GAME OVER')
            run = False

        if keys[pygame.K_RIGHT]:
            x1_change = +10
            y1_change = 0
        if keys[pygame.K_UP]:
            y1_change = -10
            x1_change = 0
        if keys[pygame.K_DOWN]:
            y1_change = +10
            x1_change = 0

    hero_x += x1_change
    hero_y += y1_change

    pygame.draw.rect(win, yellow, (hero_x, hero_y, hero_width, hero_height))
    pygame.draw.rect(win, green, (apple_x, apple_y, apple_width, apple_height))

    clock.tick(FPS)
    pygame.display.update()

pygame.quit()