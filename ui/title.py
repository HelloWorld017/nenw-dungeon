from ui.faded_element import FadedElement
import pygame


class Title(FadedElement):
    color_key = (255, 255, 255)

    # noinspection PyUnresolvedReferences
    def __init__(self, game):
        self.image = pygame.image.load('./resources/orangephobia.png')

        super().__init__(game, game.width / 2, game.height / 3,
                         self.image.get_rect().width, self.image.get_rect().height)

    def do_render(self, renderer):
        super().do_render(renderer)

        renderer.draw_image(self.image, self.width / 2, self.height / 2)
