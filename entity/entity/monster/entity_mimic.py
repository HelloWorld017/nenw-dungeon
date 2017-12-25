from entity.entity_trap import EntityTrap
from geometry.bound_box import BoundBox
from geometry.vector2 import Vector2
from render.blend import blend


class EntityMimic(EntityTrap):
    color = (190, 190, 190)
    color_front = (239, 108, 0)
    color_mimic = (245, 124, 0)
    friction = 0
    fade_tick = 0
    animation_direction = 1

    def __init__(self, game, x, y, auto_vanish=True):
        super().__init__(game, BoundBox(
            Vector2(x - 30, y - 30),
            Vector2(x + 30, y + 30)
        ))

        self.auto_vanish = auto_vanish

    def update(self, events):
        super().update(events)

        self.fade_tick += self.animation_direction

        if self.fade_tick >= 30:
            self.animation_direction = -1

        elif self.fade_tick <= 0:
            self.animation_direction = 1

        if self.auto_vanish and (not (-self.height < self.y < self.game.height + self.height)):
            self.set_dead()

    def render(self, renderer):
        fade_rate = self.fade_tick / 30

        renderer.rect(self, blend(fade_rate, self.game.background, self.color))

        renderer.polygon((
            (self.x + -10, self.y + -20), (self.x + 10, self.y + -20),
            (self.x + 10, self.y + 20), (self.x + -10, self.y + 20)
        ), blend(fade_rate, self.game.background, self.color_mimic))

        renderer.polygon((
            (self.x + -20, self.y + -10), (self.x + 20, self.y + -10),
            (self.x + 20, self.y + 10), (self.x + -20, self.y + 10)
        ), blend(fade_rate, self.game.background, self.color_front))
