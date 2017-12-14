from entity.monster.entity_trap import EntityTrap
from geometry.bound_box import BoundBox
from geometry.vector2 import Vector2
import math


class EntityBullet(EntityTrap):
    radius = 10
    color = (176, 224, 230)
    friction = 0
    bound_model_accuracy = 4

    def __init__(self, game, x, y, auto_vanish=True):
        super().__init__(game, BoundBox(
            Vector2(x - self.radius / 2, y - self.radius / 2),
            Vector2(x + self.radius / 2, y + self.radius / 2)
        ))

        self.auto_vanish = auto_vanish

    def update(self, events):
        super().update(events)

        if self.auto_vanish and ((not (-self.radius < self.x < self.game.width + self.radius)) or
                                 (not (-self.radius < self.y < self.game.height + self.radius))):

            self.set_dead()

    def render(self, renderer):
        renderer.circle(self, self.radius, self.color)

    @property
    def bound_model(self):
        return list(map(lambda theta: (
            self.x + math.cos((theta - 1 / 2) * math.pi * 2 / self.bound_model_accuracy) * self.radius,
            self.y + math.sin((theta - 1 / 2) * math.pi * 2 / self.bound_model_accuracy) * self.radius
        ), range(self.bound_model_accuracy)))
