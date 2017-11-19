from decorators.chain import chain
from ui.element import Element
from render.render import Render
import pygame


class FadedElement(Element):
    max_fade_tick = 30
    color_key = (0, 0, 255)

    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.fade_tick = 0
        self.fade_phase = "pause"
        self.surface = None
        self.surface_renderer = None

    def prepare_surface(self, width, height):
        self.surface = pygame.Surface((width, height))
        self.surface_renderer = Render(self.surface)

    @chain
    def hide(self):
        self.fade_phase = "hide"
        self.fade_tick = self.max_fade_tick

    def do_hide(self):
        super().hide()

    @chain
    def show(self):
        super().show()
        self.fade_tick = 0
        self.fade_phase = "show"

    def render(self, renderer):
        if self.fade_phase == "show":
            self.fade_tick += 1

            if self.fade_tick >= self.max_fade_tick:
                self.fade_tick = self.max_fade_tick
                self.fade_phase = "pause"

        if self.fade_phase == "hide":
            self.fade_tick -= 1

            if self.fade_tick <= 0:
                self.do_hide()
                return

        self.surface.set_alpha(self.fade_tick / self.max_fade_tick * 255)

        self.surface.fill(self.color_key)
        self.surface.set_colorkey(self.color_key)

        self.do_render(self.surface_renderer)
        renderer.draw_image(self.surface, self.x, self.y)
