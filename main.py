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



black = (0, 0, 0)
point = 0


# Устанавливаем шрифт и размер
font = pygame.font.Font(None, 74)



running = True

while running:
    screen.fill(color) # заливаем цвет окна





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                point += 1

    # отрисовка цели
    screen.blit(target_image, (target_x, target_y))

    # Создаем текстовый объект
    point_text = font.render(f'СЧЕТ {point}:0', True, black)

    # Получаем прямоугольник текста и устанавливаем его в центр
    text_rect = point_text.get_rect(center=(400, 300))

    # Отображаем текст на экране
    screen.blit(point_text, text_rect)



    pygame.display.update()



pygame.quit()



