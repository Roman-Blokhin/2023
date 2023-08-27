import pygame

SIZE = (300, 300)

pygame.display.set_mode(SIZE)
pygame.display.set_caption("Lesson one")
img = pygame.image.load('icon.png') # загружаем картинку
pygame.display.set_icon(img) # отображаем картинку

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    pygame.display.update()