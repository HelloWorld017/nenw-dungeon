import math as math
from decorators.alive import alive
from decorators.chain import chain
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
    @chain
    def teleport(self, x, y, rotation=None):
        self.x = x
        self.y = y

        if rotation is not None:
            self.rotate(rotation)

    @alive
    @chain
    def rotate(self, rotation):
        self.rot = rotation % (2 * math.pi)

    @chain
    def move(self, amount):
        self.teleport(
            self.x + math.cos(self.rot) * amount,
            self.y + math.sin(self.rot) * amount
        )

    @chain
    def turn(self, rotation):
        self.rotate(self.rot + rotation)

    @alive
    def update(self, events):
        self.x += self.motion.x
        self.y += self.motion.y

        self.motion.x *= (1 - self.friction)
        self.motion.y *= (1 - self.friction)

    @chain
    def spawn(self):
        self.entity_id = self.game.last_entity_id
        self.game.last_entity_id += 1
        self.game.entities[self.entity_id] = self

    @chain
    def set_dead(self):
        if self.entity_id is None:
            return

        self.game.death_note.append(self.entity_id)
        self.is_dead = True

    @property
    def bound_model(self):
        return self.polygon

    @alive
    def render(self, render):
        pass
