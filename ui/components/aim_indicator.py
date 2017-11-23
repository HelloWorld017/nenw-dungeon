from ui.faded_element import FadedElement
import math


class AimIndicator(FadedElement):
    color = (220, 200, 80)
    side = 50
    fade_use_transparent = False

    def __init__(self, game, player):
        super().__init__(game, player.aim, 0, self.side, self.side / 2 * math.sqrt(3))
        self.player = player

    def do_render(self, renderer):
        super().do_render(renderer)
        self.x = self.player.aim

        renderer.polygon((
            (self.x - self.width / 2, self.y),
            (self.x + self.width / 2, self.y),
            (self.x, self.y + self.height)
        ), self.blend_color(self.color))
