import pygame
pygame.init() # для того чтобы текст выводился на экран

SIZE = (600, 500)
TEXT_COLOR = (0, 155, 168)
FRAME_COLOR = (224, 255, 255)
YELLOW = (255, 255, 0)
ORANGE_RED = 255, 69, 0

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Lesson one")
img = pygame.image.load('icon.png') # загружаем картинку
pygame.display.set_icon(img) # отображаем картинку

font = pygame.font.SysFont('arial', 28) # параметры нашего шрифта
text = font.render('Подключайся к программированию', 1, TEXT_COLOR, FRAME_COLOR) # текст с параметрами, 1 - сглаживание
text_2 = font.render('Привет, Роман!', 0, YELLOW, ORANGE_RED)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.blit(text, (110, 20)) # вызываем наш текст на экран + задаем координаты х и у
    screen.blit(text_2, (0, 300))
    pygame.display.update()