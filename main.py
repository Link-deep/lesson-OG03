import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# УСТАНАВЛИВАЕМ РАЗМЕР ЭКРАНА
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# ЗАГОЛОВОК ОКНА
pygame.display.set_caption("ИГРА ТИР")


# добавляем икноку в окно
icon = pygame.image.load('image/Icon_tir.png') # Иконка
pygame.display.set_icon(icon)


# Изображение цели
target_image = pygame.image.load('image/purpose.png')

# размер изображения
target_width = 50
target_height = 50

# координаты цели
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))










running = True

while running:
    pass


pygame.quit()



