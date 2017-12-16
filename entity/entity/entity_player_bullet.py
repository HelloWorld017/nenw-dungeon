from decorators.alive import alive
from decorators.chain import chain
from entity.entity_base import Entity
from geometry.bound_box import BoundBox
from geometry.collision import test_collision
from geometry.vector2 import Vector2
import math


class EntityPlayerBullet(Entity):
    friction = 0
    height = 50
    width = 10
    speed = 30

    def __init__(self, game, x, y, color):
        super().__init__(game, BoundBox(
            Vector2(x - self.width / 2, y - self.height / 2),
            Vector2(x + self.width / 2, y + self.height / 2)
        ))

        self.color = color
        self.angle_map = self.get_angle_map()

    @chain
    def rotate(self, rotation):
        super().rotate(rotation)
        self.angle_map = self.get_angle_map()

    def get_angle_map(self):
        return (
            (math.cos(-self.rot + math.pi / 2) * self.width, math.sin(-self.rot + math.pi / 2) * self.width),
            (math.cos(-self.rot + math.pi) * self.height, math.sin(-self.rot + math.pi) * self.height),
            (math.cos(-self.rot + math.pi * 3 / 2) * self.width, math.sin(-self.rot + math.pi * 3 / 2) * self.width),
            (math.cos(-self.rot) * self.height, math.sin(-self.rot) * self.height)
        )

    @alive
    @chain
    def rotate(self, rotation):
        self.rot = (rotation + math.pi / 2) % (2 * math.pi)
        self.angle_map = self.get_angle_map()

    def update(self, events):
        super().update(events)
        self.move_invert(self.speed)

        for target in self.game.mobs:
            if test_collision(target.bound_model, self.bound_model):
                target.hurt(1)

        if self.x < 0 or self.x > self.game.width or self.y < 0 or self.y > self.game.height:
            self.set_dead()

    def render(self, renderer):
        renderer.polygon(self.bound_model, self.color)

    @property
    def bound_model(self):
        return tuple(map(lambda pos: (pos[0] + self.x, pos[1] + self.y), self.angle_map))
