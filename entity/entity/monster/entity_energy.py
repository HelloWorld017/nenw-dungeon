import geometry.math as gmath
from entity.entity_fadeable import EntityFadeable
from entity.entity_trap import EntityTrap
from geometry.bound_box import BoundBox
from geometry.vector2 import Vector2


class EntityEnergy(EntityFadeable, EntityTrap):
    color = (74, 20, 140)
    friction = 0

    def __init__(self, game, x, direction=-1):
        super().__init__(game, BoundBox(
            Vector2(x, game.height - 10),
            Vector2(x, game.height)
        ))

        self.direction = direction

        self.outer.x += self.direction * 60

        self.outer_speed = 8.5
        self.inner_speed = 9

    def update(self, events):
        super().update(events)

        self.outer.x += self.direction * self.outer_speed
        self.inner.x += self.direction * self.inner_speed
        self.fade_tick -= 0.1
        self.outer_speed -= 0.05

        if self.max.x - self.min.x < 1:
            self.max.x = self.min.x
            self.fade_set_dead(animate=False)

    def render(self, renderer):
        renderer.polygon(self.bound_model, self.blend_color(self.color))

    @property
    def outer(self):
        if self.direction == -1:
            return self.min

        return self.max

    @property
    def inner(self):
        if self.direction == -1:
            return self.max

        return self.min

    @property
    def bound_model(self):
        return gmath.rotate(self.polygon, self.rot, self)
