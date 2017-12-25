import geometry.math as gmath
from decorators.alive import alive
from decorators.chain import chain
from entity.entity_fadeable import EntityFadeable
from entity.entity_trap import EntityTrap
from geometry.bound_box import BoundBox
from geometry.vector2 import Vector2


class EntityDropper(EntityTrap, EntityFadeable):
    color = (0, 96, 100)
    friction = 0

    def __init__(self, game, x, y):
        super().__init__(game, BoundBox(
            Vector2(x - 40, y - 60),
            Vector2(x + 40, y + 60)
        ))

    def update(self, events):
        super().update(events)
        self.y = gmath.clamp(-30, self.y, self.game.height - 30)

    def render(self, renderer):
        renderer.polygon(self.bound_model, self.blend_color(self.color))

    @property
    def bound_model(self):
        return gmath.rotate(self.polygon, self.rot, self)

    @alive
    @chain
    def attack(self, target):
        target.hurt(1)
