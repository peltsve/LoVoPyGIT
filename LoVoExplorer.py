import pygame
from pygame.draw import *
pygame.init()

def draw_picture(screen, x, y, width, height):
    """ Рисует картинку с домиком на фоне травы и неба с солнцем
    :param screen: дисплей модуля pygame, на котором будет изображение дома
    :param x: координата по горизонтали
    :param y: координата по вертикали
    :param width: ширина  прямоугольника
    :param height: высота прямоугольника
    """
    print("Типа рисую картинку", x, y, width, height)
    draw_background(screen, x, y, width, height)
    house_x = x + width // 2
    house_y = y + 3 * height // 4
    house_height = min(height, width) * 2 // 3
    house_width = int(house_height*1.5)
    draw_house(screen, house_x, house_y, house_width, house_height)
    sun_radius = min(height, width)//10
    draw_sun(screen, x, y, sun_radius)
    pass
def draw_sun(screen, x, y, radius):
    print("Типа рисую солнышко: ", x, y, radius)
def draw_house(screen, x, y, width, height):
    print("Типа рисую домик: ", x, y, width, height)
def draw_background(screen, x, y, width, height):
    print("Типа рисую фон: ", x, y, width, height)

FPS = 30
width, height = screen_size = (400, 400)
screen = pygame.display.set_mode(screen_size)

draw_picture(screen,00,00,width,height)

pygame.display.update()

work_flag = True
while work_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            work_flag = False


print("Программа благополцчно завершена!")
"""
# старый домик
rect(screen, (255, 0, 255), (100, 100, 200, 200))
rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
polygon(screen, (255, 255, 0), [(100,100), (200,50),
                               (300,100), (100,100)])
polygon(screen, (0, 0, 255), [(100,100), (200,50),
                               (300,100), (100,100)], 5)
circle(screen, (0, 255, 0), (200, 175), 50)
circle(screen, (255, 255, 255), (200, 175), 50, 5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
"""