from ui.element import Element


class BlinkImage(Element):
    color_key = (240, 240, 240)
    interval = 45
    tick = 0
    is_show_phase = True

    def __init__(self, game, x, y, surface):
        super().__init__(game, x, y, surface.get_width(), surface.get_height())
        self.image = surface

    def do_render(self, renderer):
        if self.tick % self.interval == 0:
            self.is_show_phase = not self.is_show_phase

        if self.is_show_phase:
            renderer.draw_image(self.image, self.x, self.y)
