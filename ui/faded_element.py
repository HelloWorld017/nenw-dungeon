from decorators.chain import chain
from ui.element import Element
from render.render import Render
from render.blend import blend
import pygame


class FadedElement(Element):
    max_fade_tick = 30
    fade_use_transparent = True
    fade_use_left_top = False
    color_key = (0, 0, 255)

    def __init__(self, game, x, y, width, height):
        super().__init__(game, x, y, width, height)
        self.fade_tick = 0
        self.fade_phase = "pause"
        self.background = game.background
        self.surface = None
        self.surface_renderer = None

        if self.fade_use_transparent:
            self.prepare_surface()

    def prepare_surface(self):
        self.surface = pygame.Surface((self.width, self.height))
        self.surface_renderer = Render(self.surface)

    @chain
    def set_fade_tick(self, tick, status=None):
        self.fade_tick = tick

        if status is not None:
            self.fade_phase = status

    @chain
    def hide(self):
        if self.is_hidden:
            return

        self.is_hidden = True

        self.fade_phase = "hide"
        self.fade_tick = self.max_fade_tick

    def do_hide(self):
        super().hide()

    @chain
    def show(self):
        if not self.is_hidden:
            return

        self.is_hidden = False

        if self.is_pre:
            self.game.pre_ui.append(self)

        else:
            self.game.ui.append(self)

        self.fade_tick = 0
        self.fade_phase = "show"

    def render(self, renderer):
        if self.tick == 0:
            self.init_render(renderer)

        self.tick += 1

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

        use_renderer = renderer

        if self.fade_use_transparent:
            self.surface.set_alpha(self.fade_tick / self.max_fade_tick * 255)

            self.surface.fill(self.color_key)
            self.surface.set_colorkey(self.color_key)
            use_renderer = self.surface_renderer

        self.do_render(use_renderer)

        if self.fade_use_transparent:
            if self.fade_use_left_top:
                renderer.screen.blit(self.surface, (self.x, self.y))
            else:
                renderer.draw_image(self.surface, self.x, self.y)

    def blend_color(self, color):
        blend_rate = self.fade_tick / self.max_fade_tick

        return blend(blend_rate, color, self.background)

