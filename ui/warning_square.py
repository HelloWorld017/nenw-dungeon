from ui.element import Element


class WarningSquare(Element):
    is_pre = True
    warning_color = (255, 152, 0)

    def __init__(self, game, bound_box):
        super().__init__(game, bound_box.min.x, bound_box.min.y)
        self.bound_box = bound_box

    def render(self, renderer):
        renderer.rect(self.bound_box, self.warning_color)
