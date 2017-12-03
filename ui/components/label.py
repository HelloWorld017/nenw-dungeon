from decorators.chain import chain
from ui.faded_element import FadedElement


class Label(FadedElement):
    fade_use_left_top = True
    color_key = (240, 240, 240)

    def __init__(self, game, x, y, width, height, text, size, color=(20, 20, 20)):
        super().__init__(game, x, y, width, height)
        self.text = text
        self.text_image = None
        self.font = None
        self.size = size
        self.color = color
        self.text_updated = False

    def init_render(self, renderer):
        self.font = renderer.load_font(size=self.size)
        self.text_image = renderer.get_text(self.text, self.font, self.color)

    def do_render(self, renderer):
        if self.text_updated:
            self.text_image = renderer.get_text(self.text, self.font, self.color)

        renderer.screen.blit(self.text_image, (0, 0))

    @chain
    def set_text(self, text):
        self.text = text
        self.text_updated = True

    @chain
    def set_color(self, color):
        self.color = color
        self.text_updated = True
