import pygame
pygame.init() # для того чтобы текст выводился на экран

SIZE = (600, 500)
TEXT_COLOR = (0, 155, 168)
FRAME_COLOR = (224, 255, 255)
YELLOW = (255, 255, 0)
ORANGE_RED = (255, 69, 0)
BLACK = (0, 0, 0)

FPS = 60 # ЧАСТОТА КАДРОВ В СЕКУНДУ

x_1, y_1 = 0, 300

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Lesson one")
img = pygame.image.load('icon.png') # загружаем картинку
pygame.display.set_icon(img) # отображаем картинку
clock = pygame.time.Clock() # задаем кадровую частоту

font = pygame.font.SysFont('arial', 28) # параметры нашего шрифта
text = font.render('Подключайся к программированию', 1, TEXT_COLOR, FRAME_COLOR) # текст с параметрами, 1 - сглаживание
text_2 = font.render('Привет, Роман!', 0, YELLOW, ORANGE_RED)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill(BLACK) # отрисовываем черный экран, это позволит не оставлять цветные следы у движущихся предметов
    clock.tick(FPS) # передаем количество кадров для отрисовки за 1 секунду
    screen.blit(text, (110, 20)) # вызываем наш текст на экран + задаем координаты х и у
    screen.blit(text_2, (x_1, y_1))

    x_1 += 1

    pygame.display.update()