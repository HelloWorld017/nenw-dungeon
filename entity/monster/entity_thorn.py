from entity.monster.entity_trap import EntityTrap
from geometry.bound_box import BoundBox
from geometry.vector2 import Vector2


class EntityThorn(EntityTrap):
    width = 30
    height = 200

    color = (10, 190, 255)

    friction = 0

    def __init__(self, game, x, y, speed=20, inverse=False):
        self.width = game.width / 10
        self.speed = speed
        self.inverse = inverse
        self.activated = False

        super().__init__(game, BoundBox(
            Vector2(x - self.width / 2, y),
            Vector2(x + self.width / 2, y + self.height)
        ))

        if inverse:
            self.motion.y = -speed
        else:
            self.motion.y = speed

    def update(self, events):
        super().update(events)

    def render(self, renderer):
        renderer.polygon(self.bound_model, self.color)

    @property
    def bound_model(self):
        if not self.inverse:
            return (
                (self.min.x, self.min.y),
                (self.max.x, self.min.y),
                (self.x, self.max.y)
            )

        return (
            (self.min.x, self.max.y),
            (self.max.x, self.max.y),
            (self.x, self.min.y)
        )

    def attack(self, target):
        if not self.activated:
            self.activated = True
            target.hurt(1)