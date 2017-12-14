import math

from entity.entity_fadeable import EntityFadeable
from entity.monster.entity_energy import EntityEnergy
from entity.monster.entity_trap import EntityTrap
from geometry.bound_box import BoundBox
import geometry.math as gmath
from geometry.vector2 import Vector2


class EntityBomb(EntityFadeable, EntityTrap):
    color = (74, 20, 140)
    friction = 0
    speed = 10

    def __init__(self, game, x, y):
        super().__init__(game, BoundBox(
            Vector2(x - 10, y - 30),
            Vector2(x + 10, y + 30)
        ))

    def update(self, events):
        super().update(events)
        self.move_invert(self.speed)

        if self.y >= self.game.height - math.sin(self.rot) * 30:
            self.set_dead()

    def set_dead(self):
        if self.is_dead_anim_in_progress:
            return

        super().set_dead()

        EntityEnergy(self.game, self.x, direction=-1).spawn()
        EntityEnergy(self.game, self.x, direction=1).spawn()

    def render(self, renderer):
        renderer.polygon(self.bound_model, self.blend_color(self.color))

    @property
    def bound_model(self):
        return gmath.rotate(self.polygon, self.rot + math.pi / 2, self)
