import pygame as pg


WIDTH = 400
HEIGHT = 500
FPS = 30

RED = 255, 0, 0
GREEN = 0, 100, 0
BLUE = 0, 0, 255
PINK = 255, 0, 255
YELLOW = 255, 255, 0
SKY = 0, 175, 255
WHITE = 255, 255, 255
BLACK = 0, 0, 0

x = 10
y = 10
mouse_x = 200
mouse_y = 400
eye_l_x = 50
eye_l_y = 50
eye_r_x = 140
eye_r_y = 50

width = 20
height = 20

velocity = 0.1


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('WarCraft')


run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and x > 0:
        mouse_x -= velocity
        eye_l_x -= velocity/4.5
        eye_r_x -= velocity/4

    elif keys[pg.K_RIGHT] and x < 300:
        mouse_x += velocity
        eye_l_x += velocity/4
        eye_r_x += velocity/4.5

    elif keys[pg.K_UP] and x > 0:
        mouse_y -= velocity
        eye_l_y -= velocity/4.5
        eye_r_y -= velocity/4

    elif keys[pg.K_DOWN] and x < 300 :
        mouse_y += velocity
        eye_l_y += velocity/4
        eye_r_y += velocity/4

    screen.fill(GREEN) # пишем в цикле, чтобы объект не растягивался

    first = pg.draw.rect(screen, BLACK, (10, 10, WIDTH/2, HEIGHT/2))
    second = pg.draw.rect(screen, WHITE, (eye_l_x, eye_l_y, width, height))
    third = pg.draw.rect(screen, WHITE, (eye_r_x, eye_r_y, width, height))
    four = pg.draw.rect(screen, BLACK, (mouse_x, mouse_y, width, height))
    pg.display.update()


pg.quit()

