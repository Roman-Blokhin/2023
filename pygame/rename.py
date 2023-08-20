import pygame

red = 100, 0, 0
green = 0, 100, 0
yellow = 250, 250, 0
blue = 0, 0, 100

screen_width = 300
screen_height = 400
FPS = 30

run = True

hero_width = 20
hero_height = 20

hero_x = screen_width/2
hero_y = screen_height/2

velocity = 0.1

pygame.init()
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('WarCraft')

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and hero_x > 5:
        hero_x -= velocity

    if keys[pygame.K_RIGHT] and hero_x + hero_width < screen_width - 4:
        hero_x += velocity

    if keys[pygame.K_UP] and hero_y > 5:
        hero_y -= velocity

    if keys[pygame.K_DOWN] and hero_y + hero_height < screen_height - 4:
        hero_y += velocity

    win.fill(red)
    pygame.draw.rect(win, yellow, (hero_x, hero_y, hero_width, hero_height))
    pygame.display.update()

pygame.quit()