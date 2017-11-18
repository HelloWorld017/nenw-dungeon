import sys
import pygame
from pygame import gfxdraw
from pygame.locals import *
from geometry.collision import test_collision

pygame.init()

screen = pygame.display.set_mode((1280, 720), DOUBLEBUF)
pygame.display.set_caption('Collision Tester')


FPS = 30

clock = pygame.time.Clock()
font = pygame.font.Font("../resources/NanumSquareL.ttf", 32)


def write_text(x, y, text_content):
    text_color = (20, 20, 20)
    text_surface = font.render(text_content, True, text_color)

    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)

    screen.blit(text_surface, text_rect)

polygons = [[], []]
polygon_colors = [(233, 30, 99), (3, 169, 244)]
intercept = -1


def check_intercept():
    global intercept

    if test_collision(polygons[0], polygons[1]):
        intercept = 1

    else:
        intercept = 0


while True:
    background = (240, 240, 240)
    screen.fill(background)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_r:
                intercept = -1
                polygons = [[], []]

            if event.key == K_d:
                check_intercept()

        if event.type == MOUSEBUTTONDOWN:
            polygon_num = None

            if pygame.key.get_pressed()[K_1]:
                polygon_num = 0

            elif pygame.key.get_pressed()[K_2]:
                polygon_num = 1

            if polygon_num is None:
                continue

            intercept = -1
            polygons[polygon_num].append((event.pos[0], event.pos[1]))

    for i in range(2):
        for dot in polygons[i]:
            gfxdraw.aacircle(screen, dot[0], dot[1], 5, polygon_colors[i])
            gfxdraw.filled_circle(screen, dot[0], dot[1], 5, polygon_colors[i])

        if len(polygons[i]) >= 3:
            gfxdraw.aapolygon(screen, tuple(polygons[i]), polygon_colors[i])
            gfxdraw.filled_polygon(screen, tuple(polygons[i]), polygon_colors[i])

    text = "Not determined."

    if intercept == 1:
        text = "Collides!"

    elif intercept == 0:
        text = "Not collides."

    write_text(640, 640, text)

    pygame.display.flip()
    clock.tick(FPS)
