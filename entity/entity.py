import math as math
from decorators.alive import alive
from geometry.bound_box import BoundBox
from geometry.vector2 import Vector2


class Entity(BoundBox):
    friction = 0.3
    is_dead = False

    def __init__(self, game, bound_box):
        super().__init__(bound_box.min, bound_box.max)
        self.game = game
        self.rot = 0
        self.motion = Vector2(0, 0)
        self.entity_id = None

    @alive
    def teleport(self, x, y, rotation=None):
        self.x = x
        self.y = y

        if rotation is not None:
            self.rotate(rotation)

    @alive
    def rotate(self, rotation):
        self.rot = rotation % (2 * math.pi)

    def move(self, amount):
        self.teleport(self.x + math.cos(self.rot) * amount, self.y + math.sin(self.rot) * amount)

    def turn(self, rotation):
        self.rotate(self.rot + rotation)

    @alive
    def update(self, events):
        self.x += self.motion.x
        self.y += self.motion.y

        self.motion.x *= self.friction
        self.motion.y *= self.friction

    def spawn(self):
        self.game.entities[self.game.last_entity_id] = self
        self.game.last_entity_id += 1

    def set_dead(self):
        if self.entity_id is None:
            return

        self.game.entities.pop(self.entity_id, None)
        self.is_dead = True

    @alive
    def render(self, render):
        pass
