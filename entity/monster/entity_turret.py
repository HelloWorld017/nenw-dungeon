import math

from entity.monster.entity_bullet import EntityBullet
from entity.monster.entity_trap import EntityTrap
from geometry.bound_box import BoundBox
import geometry.math as gmath
from geometry.vector2 import Vector2


class EntityTurret(EntityTrap):
    color = (176, 224, 230)
    friction = 0
    fire_tick = 20
    speed = 20
    size = 30

    def __init__(self, game, x, y, target):
        super().__init__(game, BoundBox(
            Vector2(x - self.size, y - self.size),
            Vector2(x + self.size, y + self.size)
        ))

        self.target = target

    def update(self, events):
        super().update(events)

        if self.entity_inner_tick % self.fire_tick == 0:
            turret_position = gmath.rotate((
                (self.x, self.y - self.size),
            ), self.rot, self)

            bullet = EntityBullet(self.game, turret_position[0][0], turret_position[0][1]).spawn()
            theta = math.atan2((self.target.y - turret_position[0][1]), (self.target.x - turret_position[0][0]))
            bullet.color = (0, 184, 212)

            bullet.motion.set_x(math.cos(theta) * self.speed).set_y(math.sin(theta) * self.speed)

    def render(self, renderer):
        renderer.polygon(self.polygon, self.color)

    @property
    def polygon(self):
        return gmath.rotate((
            (self.x - self.size, self.y + self.size),
            (self.x + self.size, self.y + self.size),
            (self.x + self.size / 6, self.y + self.size / 6),
            (self.x + self.size / 6, self.y - self.size),
            (self.x - self.size / 6, self.y - self.size),
            (self.x - self.size / 6, self.y + self.size / 6)
        ), self.rot + math.pi, self)
