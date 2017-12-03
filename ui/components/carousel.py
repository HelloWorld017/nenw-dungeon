from collections import deque

from decorators.propagate_event import propagate_event
from keyboard.keys import Keys
from render.tween import Tween
from ui.faded_element import FadedElement

import pygame.locals as pg_vars


@propagate_event
class Carousel(FadedElement):
    DIRECTION_UP = -1
    DIRECTION_DOWN = 1

    fade_use_left_top = True
    color_key = (240, 240, 240)
    gap = 50
    ui_event = True

    def __init__(self, game, x, y, width, height, elements):
        super().__init__(game, x, y, width, height)
        self.elements = deque(list(map(
                lambda elem: Tween(elem, {
                        'y': elem.y,
                        'opacity': 0
                    }, ['y']).set_on_update(
                        lambda ev: elem.update_event(ev) if elem.ui_event else None
                    ),
                elements
            )
        ))

        for element in (self.elements[0], self.elements[2]):
            element.set_value('opacity', 128, 15)

        self.elements[1].set_value('opacity', 255, 15)
        self.elements[1].element.activated = True

        self.recalculate_positions(1)

    def render(self, renderer):
        for elem in self.elements:
            elem.update()
            elem.element\
                .set_fade_tick(elem.value['opacity'] / 255 * elem.element.max_fade_tick, "pause")\
                .render(renderer)

    def scroll(self, direction=None):
        # Default direction is up
        if direction is None:
            direction = self.DIRECTION_UP

        if direction == self.DIRECTION_UP:
            first = 0
            last = 2
        else:
            first = 2
            last = 0

        self.elements[first].set_value('opacity', 0, 15)
        self.elements[1].element.activated = False

        self.elements.rotate(direction)

        self.recalculate_positions(15)
        self.elements[first].set_value('opacity', 128, 15)
        self.elements[1].set_value('opacity', 255, 15)
        self.elements[1].element.activated = True
        self.elements[last].set_value('opacity', 128, 15)

    def recalculate_positions(self, tick):
        for index, elem in enumerate(self.elements):
            elem.set_value('y', self.get_desired_y(index, elem), tick)

    def get_desired_y(self, index, elem):
        return self.y + (elem.element.height + self.gap) * (index - 1)

    def do_update_event(self, ev):
        if ev.type == pg_vars.KEYDOWN:
            if ev.key == Keys.KEY_SKILL_UI_UP:
                self.scroll(self.DIRECTION_DOWN)

            elif ev.key == Keys.KEY_SKILL_UI_DOWN:
                self.scroll(self.DIRECTION_UP)

    @property
    def activated_element(self):
        return self.elements[1].element
