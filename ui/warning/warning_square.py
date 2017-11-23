from ui.faded_element import FadedElement


class WarningSquare(FadedElement):
    is_pre = True
    fade_use_transparent = False
    warning_color = (255, 204, 128)

    def __init__(self, game, bound_box):
        super().__init__(game, bound_box.x, bound_box.y, bound_box.width, bound_box.height)
        self.bound_box = bound_box

    def do_render(self, renderer):
        super().do_render(renderer)
        renderer.rect(self.bound_box, self.blend_color(self.warning_color))
