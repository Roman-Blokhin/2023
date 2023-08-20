import pygame as pg


WIDTH_SCREEN = 400
HEIGHT_SCREEN = 500
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

hero_x = 200
hero_y = 400
hero_width = 20 # ширина героя, нужна, чтобы не выходил за границы экрана
hero_height = 20 # высота героя, нужна, чтобы не выходил за границы экрана

eye_l_x = 50
eye_l_y = 50
eye_l_width = 20
eye_l_height = 20

eye_r_x = 140
eye_r_y = 50
eye_r_width = 20
eye_r_height = 20

velocity = 0.1


pg.init()
screen = pg.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
pg.display.set_caption('WarCraft')


run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and hero_x >= 0:
        hero_x -= velocity
        eye_l_x -= velocity/4.5
        eye_r_x -= velocity/4

    elif keys[pg.K_RIGHT] and hero_x + hero_width < WIDTH_SCREEN:
        hero_x += velocity
        eye_l_x += velocity/4
        eye_r_x += velocity/4.5

    elif keys[pg.K_UP] and hero_y > 300:
        hero_y -= velocity
        eye_l_y += velocity/7.5
        eye_r_y += velocity/7

    elif keys[pg.K_DOWN] and hero_y + hero_height < HEIGHT_SCREEN:
        hero_y += velocity
        eye_l_y -= velocity/7
        eye_r_y -= velocity/7

    screen.fill(GREEN) # пишем в цикле, чтобы объект не растягивался

    first = pg.draw.rect(screen, BLACK, (10, 10, WIDTH_SCREEN/2, HEIGHT_SCREEN/2))
    second = pg.draw.rect(screen, WHITE, (eye_l_x, eye_l_y, eye_l_width, eye_l_height))
    third = pg.draw.rect(screen, WHITE, (eye_r_x, eye_r_y, eye_r_width, eye_r_height))
    four = pg.draw.rect(screen, BLACK, (hero_x, hero_y, hero_width, hero_height))
    pg.display.update()


pg.quit()

