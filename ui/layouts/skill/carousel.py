from collections import deque
from render.tween import Tween
from ui.faded_element import FadedElement


class Carousel(FadedElement):
    DIRECTION_UP = -1
    DIRECTION_DOWN = 1

    color_key = (240, 240, 240)
    gap = 50

    def __init__(self, game, x, y, width, height, elements):
        super().__init__(game, x, y, width, height)
        self.elements = deque(list(map(lambda elem: Tween(elem, {
            'y': elem.y,
            'opacity': 0
        }, ['y']), elements)))

        for element in self.elements[0:3]:
            element.set_value('opacity', 255, 30)

        self.recalculate_positions(1)

        self.height = elements[0].height

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

        self.elements[first].set_value('opacity', 0, 30)

        def show_callback():
            self.elements[last].set_value('opacity', 255, 30)

        def callback():
            deque(self.elements).rotate(direction)
            self.recalculate_positions(30)
            self.elements[last].set_callback(show_callback)

        self.elements[first].set_callback(callback)

    def recalculate_positions(self, tick):
        for index, elem in enumerate(self.elements):
            elem.set_value('y', self.get_desired_y(index, elem), tick)

    def get_desired_y(self, index, elem):
        return (self.height + self.gap) * (index - 1) + elem.height / 2

