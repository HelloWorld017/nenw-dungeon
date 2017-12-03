from decorators.chain import chain
from geometry.vector2 import Vector2
import pygame
from pygame import gfxdraw

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = "./resources/KoPubDotumLight.ttf"


class Render(object):
    def __init__(self, screen):
        self.screen = screen

    @chain
    def write_text(self, x, y, text, font=FONT, color=WHITE, size=32):
        font_object = self.load_font(font, size)
        text_surface = self.get_text(text, font_object, color)

        self.draw_image(text_surface, x, y)

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
        gfxdraw.aacircle(self.screen, int(vector.x), int(vector.y), int(radius), color)

        if fill:
            gfxdraw.filled_circle(self.screen, int(vector.x), int(vector.y), int(radius), color)

        if width != 1:
            pygame.draw.circle(self.screen, color, vector.pos, int(radius), width)

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

        elif width != 1:
            pygame.draw.polygon(self.screen, color, polygon, width)

    @staticmethod
    def update():
        pygame.display.flip()

    @staticmethod
    def load_font(font=FONT, size=32):
        return pygame.font.Font(font, size)

    @staticmethod
    def get_text(text, font, color=WHITE):
        text_surface = font.render(text, True, color)

        return text_surface

    # noinspection PyTypeChecker
    @staticmethod
    def get_paragraph_text(text, font, width, height, color=WHITE):
        final_surface = pygame.Surface((width, height))
        final_surface.set_colorkey((240, 240, 240))
        final_surface.fill((240, 240, 240))
        final_surface.set_alpha(255)

        words = text.split(' ')

        line_map = [{
            'space': None,
            'words': [],
            'width': 0,
            'height': 0
        }]

        working_line = 0
        line_height = 1.2
        min_space = font.size(' ')[0]

        if len(words) == 0:
            return final_surface

        def finalize_line():
            nonlocal working_line

            if not len(words) == 1:
                additional_space = (width - line_map[working_line]['width']) / (len(words) - 1)
            else:
                additional_space = 0

            line_map[working_line]['space'] = min_space + additional_space
            working_line += 1

            line_map.append({
                'space': None,
                'words': [],
                'width': 0,
                'height': 0
            })

        for word_index, word in enumerate(words):
            word_width = sum((font.size(i)[0] for i in word))
            word_height = max((font.size(i)[1] for i in word))

            if not width - line_map[working_line]['width'] > word_width:
                line_map[working_line]['width'] -= min_space
                finalize_line()

            if width - line_map[working_line]['width'] > word_width:
                line_map[working_line]['words'].append({
                    'text': word,
                    'size': word_width
                })

                line_map[working_line]['width'] += word_width

                if line_map[working_line]['height'] < word_height:
                    line_map[working_line]['height'] = word_height

                if width - line_map[working_line]['width'] > min_space:
                    line_map[working_line]['width'] += min_space

                    if word_index + 1 == len(words):
                        finalize_line()

                else:
                    finalize_line()

        line_map.pop()

        # Remove additional space
        line_map[len(line_map) - 1]['space'] = min_space

        x = 0
        y = 0

        for line in line_map:
            words = line['words']

            for word in words:
                final_surface.blit(Render.get_text(word['text'], font, color), (x, y))
                x += word['size'] + line['space']

            x = 0
            y += line['height'] * line_height
        return final_surface
