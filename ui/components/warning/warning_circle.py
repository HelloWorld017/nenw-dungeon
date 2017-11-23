from ui.faded_element import FadedElement


class WarningCircle(FadedElement):
    is_pre = True
    fade_use_transparent = False
    warning_color = (255, 204, 128)

    def __init__(self, game, pos, radius):
        super().__init__(game, pos.x, pos.y, radius * 2, radius * 2)
        self.pos = pos.clone()
        self.radius = radius

    def do_render(self, renderer):
        super().do_render(renderer)

        # renderer.circle(self.pos, self.radius, self.warning_color, fill=False, width=5)
        renderer.circle(self.pos, self.radius, self.blend_color(self.warning_color))
