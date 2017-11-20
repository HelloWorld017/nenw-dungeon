from geometry.vector2 import Vector2
from ui.faded_element import FadedElement


class WarningCircle(FadedElement):
    is_pre = True
    warning_color = (255, 152, 0)

    def __init__(self, game, pos, radius):
        super().__init__(game, pos.x, pos.y)
        self.pos = pos
        self.radius = radius
        self.center_pos = Vector2(self.radius, self.radius)
        self.prepare_surface(self.radius * 2, self.radius * 2)

    def do_render(self, renderer):
        super().do_render(renderer)

        # renderer.circle(self.pos, self.radius, self.warning_color, fill=False, width=5)
        renderer.circle(self.center_pos, self.radius, self.warning_color)
