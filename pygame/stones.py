import random as ra
import pygame

black = (0, 0, 0)
white = (255, 255, 255)
red = (150, 0, 0)
green = (0, 150, 0)
blue = (0, 0, 150)

block_size = 100
margin = 50
width = height = block_size*2 + margin*3
size = (width, height)

firstNumber = ra.randint(1, 6)
secondNumber = ra.randint(1, 6)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('stones..')

print('Первый кубик: ', str (firstNumber))
print('Второй кубик: ', str (secondNumber))