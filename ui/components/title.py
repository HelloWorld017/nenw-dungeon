from ui.faded_element import FadedElement
import pygame


class Title(FadedElement):
    color_key = (255, 255, 255)

    # noinspection PyUnresolvedReferences
    def __init__(self, game):
        super().__init__(game, game.width / 2, game.height / 2, game.width, game.height)

        self.image = pygame.image.load('./resources/orangephobia.png')
        self.explanation = pygame.image.load('./resources/explanation.png')

    def do_render(self, renderer):
        super().do_render(renderer)

        renderer.draw_image(self.explanation, self.width / 2, self.height / 2)
        renderer.draw_image(self.image, self.width / 2, self.height / 3)
