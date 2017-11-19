from ui.faded_element import FadedElement


class WarningCircle(FadedElement):
    is_pre = True
    warning_color = (255, 152, 0)

    def __init__(self, game, pos, radius):
        super().__init__(game, pos.x, pos.y)
        self.pos = pos
        self.radius = radius
        self.prepare_surface(self.radius, self.radius)

    def do_render(self, renderer):
        super().do_render(renderer)

        renderer.circle(self.pos, self.radius, self.warning_color, fill=False, width=5)
        renderer.circle(self.pos, self.radius / 2, self.warning_color)
