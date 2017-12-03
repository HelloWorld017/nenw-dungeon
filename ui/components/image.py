from ui.faded_element import FadedElement


class Image(FadedElement):
    color_key = (240, 240, 240)
    fade_use_left_top = True

    def __init__(self, game, x, y, surface, top_left=True):
        super().__init__(game, x, y, surface.get_width(), surface.get_height())
        self.image = surface
        self.top_left = top_left

    def do_render(self, renderer):
        if self.top_left:
            renderer.screen.blit(self.image, (0, 0))

        else:
            renderer.draw_image(self.image, 0, 0)
