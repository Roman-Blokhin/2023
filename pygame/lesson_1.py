import pygame
pygame.init() # для того чтобы текст выводился на экран

SIZE = (600, 500)
TEXT_COLOR = (0, 155, 168)
FRAME_COLOR = (224, 255, 255)
YELLOW = (255, 255, 0)
ORANGE_RED = (255, 69, 0)
BLACK = (0, 0, 0)

FPS = 150 # ЧАСТОТА КАДРОВ В СЕКУНДУ

x_1, y_1 = 0, 300 # координаты второй надписи
x_2, y_2 = 120, 20

direct_x = 1
direct_y = 1

direct_x_2 = 0.5
direct_y_2 = 1

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Lesson one")
img = pygame.image.load('icon.png') # загружаем картинку
pygame.display.set_icon(img) # отображаем картинку
clock = pygame.time.Clock() # задаем кадровую частоту

font = pygame.font.SysFont('arial', 28) # параметры нашего шрифта
text = font.render('Подключайся к программированию', 1, TEXT_COLOR, FRAME_COLOR) # текст с параметрами, 1 - сглаживание
text_2 = font.render('Привет, Роман!', 0, YELLOW, ORANGE_RED)

width_1, height_1 = text_2.get_size() # УЗНАЕМ ШИРИНУ НАШЕЙ ЗАПИСИ, ЧТОБЫ ИСПОЛЬЗОВАТЬ В ЦИКЛЕ
width_2, height_2 = text.get_size()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill(BLACK) # отрисовываем черный экран, это позволит не оставлять цветные следы у движущихся предметов
    clock.tick(FPS) # передаем количество кадров для отрисовки за 1 секунду
    screen.blit(text, (x_2, y_2)) # вызываем наш текст на экран + задаем координаты х и у
    screen.blit(text_2, (x_1, y_1))

    x_1 += direct_x
    y_1 += direct_y
    if x_1 + width_1 >= SIZE[0] or x_1 < 0:
        direct_x = -direct_x # условие, чтобы запись развернулась и пошла назад

    if y_1 + height_1 >= SIZE[1] or y_1 < 0:
        direct_y = -direct_y

    x_2 += direct_x_2
    y_2 += direct_y_2
    if x_2 + width_2 >= SIZE[0] or x_2 < 0:
        direct_x_2 = -direct_x_2 # условие, чтобы запись развернулась и пошла назад

    if y_2 + height_2 >= SIZE[1] or y_2 < 0:
        direct_y_2 = -direct_y_2




    pygame.display.update()