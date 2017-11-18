from ui.element import Element
import math


class HealthBar(Element):
    width = 200
    height = 50
    color = (0, 188, 212)
    skew = math.pi / 3
    ratio = 1 / 3

    def __init__(self, game, x, y, player):
        super().__init__(game, x, y)
        self.player = player
        self.skew_x = 1 / math.tan(self.skew) * self.height
        self.real_width = self.width - self.skew_x
        self.sector_width = self.real_width / (self.player.max_health * (1 + self.ratio) - self.ratio)

    def render(self, renderer):
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

                color=self.color
            )



