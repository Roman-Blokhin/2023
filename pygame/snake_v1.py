import pygame
import random
pygame.init()

red = 100, 0, 0
green = 0, 250, 0
yellow = 250, 250, 0
blue = 0, 0, 100
black = 0, 0, 0
white = 255, 255, 255
grey = 55, 55, 55

screen_width = 300
screen_height = 400
FPS = 7

snake_block = 10
snake_speed = 10

second_win = pygame.font.SysFont(None, 30) # создали слой для сообщения, которое высветится поверх экрана

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('WarCraft')
clock = pygame.time.Clock()

def message (msg, color): # создаем функцию для появления сообщения по окончанию игры
    mesg = second_win.render(msg, True, color) # добавляем слой
    win.blit(mesg, [50, 200]) # отрисовываем сообщение на основной поверхности

def gameloop (): # функция, которая не закрывает игру при проигрыше, а предлагает ее продолжить
    game_over = False
    game_close = False

    x1_change = 0
    y1_change = 0

    hero_x = screen_width/2
    hero_y = screen_height/2
    hero_width = 20
    hero_height = 20

    foodx = round(random.randint(0, screen_width - snake_block) / 10.0) * 10.0 # координаты еды х
    foody = round(random.randint(0, screen_height - snake_block) / 10.0) * 10.0 # координаты еды у

    while not game_over:
        while game_close:
            win.fill(black) # установил слой заливки поверх экрана цикла
            message('SPASE - новая игра', white) # вызываем функцию с завершающим сообщением
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameloop ()

        win.fill(red)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                x1_change = - snake_block
                y1_change = 0
            if keys[pygame.K_RIGHT]:
                x1_change = snake_block
                y1_change = 0
            if keys[pygame.K_UP]:
                y1_change = - snake_block
                x1_change = 0
            if keys[pygame.K_DOWN]:
                y1_change = snake_block
                x1_change = 0

        if hero_x + hero_width >= screen_width or hero_x <= 0 or hero_y + hero_height >= screen_height or hero_y <= 0:
            print('GAME OVER')
            game_close = True

        hero_x += x1_change
        hero_y += y1_change

        pygame.draw.rect(win, yellow, (hero_x, hero_y, hero_width, hero_height))
        pygame.draw.rect(win, green, (foodx, foody, hero_width, hero_height))

        if hero_x == foodx and hero_y == foody:
            print('Скушал')
        clock.tick(snake_speed)

        clock.tick(FPS)
        pygame.display.update()

    pygame.quit()
    quit()

gameloop()