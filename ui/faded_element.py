from decorators.chain import chain
from ui.element import Element


class FadedElement(Element):
    max_fade_tick = 30

    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.fade_tick = None

    @chain
    def hide(self):
        self.fade_tick = self.max_fade_tick

    def do_hide(self):
        super().hide()

    def render(self, renderer):
        if self.fade_tick <= 0:
            pass
            #TODO
