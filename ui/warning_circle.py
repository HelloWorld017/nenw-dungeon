from ui.element import Element


class WarningCircle(Element):
    is_pre = True
    warning_color = (255, 152, 0)

    def __init__(self, game, pos, radius):
        super().__init__(game, pos.x, pos.y)
        self.pos = pos
        self.radius = radius

    def render(self, renderer):
        renderer.circle(self.pos, self.radius, self.warning_color, fill=False, width=5)
        renderer.circle(self.pos, self.radius / 2, self.warning_color)
