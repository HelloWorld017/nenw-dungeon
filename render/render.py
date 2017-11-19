from decorators.chain import chain
from geometry.vector2 import Vector2
import pygame
from pygame import gfxdraw

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Render(object):
    def __init__(self, screen):
        self.screen = screen

    @chain
    def write_text(self, x, y, text, font=None, color=WHITE, size=32):
        font = pygame.font.Font(font, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    @chain
    def draw_image(self, image, x, y, degree=0):
        rotated = pygame.transform.rotate(image, degree)
        rect = rotated.get_rect()
        rect.center = (x, y)
        self.screen.blit(rotated, rect)

    @chain
    def fill(self, color=BLACK):
        self.screen.fill(color)

    @chain
    def rect(self, bound_box, color=WHITE, fill=True):
        self.polygon(bound_box.polygon, color, fill)

    @chain
    def circle(self, vector, radius, color=WHITE, fill=True, width=1):
        gfxdraw.aacircle(self.screen, vector.x, vector.y, radius, color)

        if fill:
            gfxdraw.filled_circle(self.screen, vector.x, vector.y, radius, color)

        if width != 1:
            pygame.draw.circle(self.screen, color, vector.pos, radius, width)

    @chain
    def line(self, pos1, pos2, color=WHITE):
        pygame.draw.aaline(self.screen, color, pos1.pos, pos2.pos)

    @chain
    def polygon(self, pos_list, color=WHITE, fill=True, width=1):
        if not len(pos_list) > 0:
            return

        if isinstance(pos_list[0], Vector2):
            polygon = tuple(map(
                lambda vec: vec.pos,
                pos_list
            ))
        else:
            polygon = pos_list

        gfxdraw.aapolygon(self.screen, polygon, color)

        if fill:
            gfxdraw.filled_polygon(self.screen, polygon, color)

        if width != 1:
            pygame.draw.polygon(self.screen, color, polygon, width)

    @staticmethod
    def update():
        pygame.display.flip()
