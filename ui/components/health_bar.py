from ui.faded_element import FadedElement
import math


class HealthBar(FadedElement):
    color = (0, 188, 212)
    skew = math.pi / 3
    ratio = 1 / 3

    fade_use_transparent = False

    def __init__(self, game, x, y, player):
        super().__init__(game, x, y, 400, 50)
        self.player = player
        self.skew_x = 1 / math.tan(self.skew) * self.height
        self.real_width = self.width - self.skew_x
        self.sector_width = self.real_width / (self.player.max_health * (1 + self.ratio) - self.ratio)

    def do_render(self, renderer):
        # Render borders
        for i in range(self.player.health):
            previous_width = self.sector_width * (1 + self.ratio) * i

            renderer.polygon(
                (
                    (self.x + previous_width + self.skew_x, self.y),
                    (self.x + previous_width + self.sector_width + self.skew_x, self.y),
                    (self.x + previous_width + self.sector_width, self.y + self.height),
                    (self.x + previous_width, self.y + self.height)
                ),

                color=self.blend_color(self.color)
            )

