import pygame


class Render(object):
    def __init__(self, screen):
        self.screen = screen

    def write_text(self, x, y, text, font=None, color=(255, 255, 255), size=32):
        font = pygame.font.Font(font, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw_image(self, image, x, y, degree):
        rotated = pygame.transform.rotate(image, degree)
        rect = rotated.get_rect()
        rect.center = (x, y)
        self.screen.blit(rotated, rect)

    def fill(self, color=(0, 0, 0)):
        self.screen.fill(color)

    def rect(self, bound_box, color=(255, 255, 255)):
        pygame.draw.rect(self.screen, color, bound_box.rect)

    def circle(self, vector, radius, color=(255, 255, 255)):
        pygame.draw.circle(self.screen, color, vector.pos, radius)

    def line(self, pos1, pos2, color=(255, 255, 255)):
        pygame.draw.line(self.screen, color, pos1.pos, pos2.pos)

    def polygon(self, pos_list, color=(255, 255, 255)):
        pass

    @staticmethod
    def update():
        pygame.display.flip()
