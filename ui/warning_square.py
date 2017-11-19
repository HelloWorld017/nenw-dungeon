from geometry.vector2 import Vector2
from ui.faded_element import FadedElement


class WarningSquare(FadedElement):
    is_pre = True
    warning_color = (255, 152, 0)

    def __init__(self, game, bound_box):
        super().__init__(game, bound_box.x, bound_box.y)
        self.prepare_surface(bound_box.width, bound_box.height)
        self.bound_box = bound_box
        self.local_bound_box = bound_box.clone().subtract(Vector2(bound_box.x - bound_box.width / 2, 0))

    def do_render(self, renderer):
        super().do_render(renderer)
        renderer.rect(self.local_bound_box, self.warning_color)
