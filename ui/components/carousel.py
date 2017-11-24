from collections import deque

from render.tween import Tween
from ui.faded_element import FadedElement

import pygame.locals as pg_vars


class Carousel(FadedElement):
    DIRECTION_UP = -1
    DIRECTION_DOWN = 1

    fade_use_left_top = True
    color_key = (240, 240, 240)
    gap = 50
    ui_event = True

    def __init__(self, game, x, y, width, height, elements):
        super().__init__(game, x, y, width, height)
        self.elements = deque(list(map(lambda elem: Tween(elem, {
            'y': elem.y,
            'opacity': 0
        }, ['y']), elements)))

        for element in (self.elements[0], self.elements[2]):
            element.set_value('opacity', 128, 15)

        self.elements[1].set_value('opacity', 255, 15)

        self.recalculate_positions(1)

    def render(self, renderer):
        for elem in self.elements:
            elem.update()
            elem.element.fade_phase = "pause"
            elem.element.fade_tick = elem.value['opacity'] / 255 * elem.element.max_fade_tick
            elem.element.render(renderer)

    def scroll(self, direction=None):
        # Default direction is up
        if direction is None:
            direction = self.DIRECTION_UP
            first = 0
            last = 2
        else:
            first = 2
            last = 0

        self.elements[first].set_value('opacity', 0, 15)
        self.elements.rotate(direction)
        self.recalculate_positions(15)
        self.elements[first].set_value('opacity', 128, 15)
        self.elements[1].set_value('opacity', 255, 15)
        self.elements[last].set_value('opacity', 128, 15)

    def recalculate_positions(self, tick):
        for index, elem in enumerate(self.elements):
            elem.set_value('y', self.get_desired_y(index, elem), tick)

    def get_desired_y(self, index, elem):
        return self.y + (elem.element.height + self.gap) * (index - 1)

    def update_event(self, ev):
        if ev.type == pg_vars.KEYDOWN:
            if ev.key == pg_vars.K_UP:
                self.scroll(self.DIRECTION_UP)

            elif ev.key == pg_vars.K_DOWN:
                self.scroll(self.DIRECTION_DOWN)

        for elem in self.elements:
            if elem.element.ui_event:
                elem.element.update_event(ev)
