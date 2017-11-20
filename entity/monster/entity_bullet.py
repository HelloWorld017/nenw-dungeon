from entity.monster.entity_trap import EntityTrap
from geometry.bound_box import BoundBox
from geometry.vector2 import Vector2
import math


class EntityBullet(EntityTrap):
    radius = 10
    color = (176, 224, 230)
    friction = 0

    def __init__(self, game, x, y):
        super().__init__(game, BoundBox(
            Vector2(x - self.radius / 2, y - self.radius / 2),
            Vector2(x + self.radius / 2, y + self.radius / 2)
        ))

    def update(self, events):
        super().update(events)

    def render(self, renderer):
        renderer.circle(self, self.radius, self.color)

    @property
    def bound_model(self):
        return list(map(lambda theta: (self.x + math.cos((theta - 1 / 2) * math.pi / 3) * self.radius,
                                  self.y + math.sin((theta - 1 / 2) * math.pi / 3) * self.radius), range(6)))

    def attack(self, target):
        target.hurt(1)
