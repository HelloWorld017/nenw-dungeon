from entity.entity import Entity
from geometry.bound_box import BoundBox
from geometry.vector2 import Vector2
import geometry.math as gmath
from keyboard.keys import Keys
import pygame.locals as pg_vars

import math


class Player(Entity):
    friction = 0.3
    air_jump = False
    jump_start = 0
    jump_count = 0

    def __init__(self, game):
        super().__init__(game, BoundBox(
            Vector2(game.width / 2 - 25, game.height - 50),
            Vector2(game.width / 2 + 25, game.height)
        ))

    def render(self, renderer):
        super().render(renderer)
        renderer.rect(self, (220, 200, 80))

    def do_jump(self):
        if self.air_jump and self.is_ground:
            return

        if self.jump_count >= 2:
            return

        self.jump_start = 10
        self.jump_count += 1

    @property
    def is_ground(self):
        return self.max.y >= self.game.height

    def update(self, events):
        super().update(events)
        if self.game.key_maps[Keys.KEY_LEFT]:
            self.rotate(math.pi)
            self.move(15)

        if self.game.key_maps[Keys.KEY_RIGHT]:
            self.rotate(0)
            self.move(15)

        for event in events:
            if event.type is pg_vars.KEYDOWN:
                if event.key is Keys.KEY_JUMP:
                    self.do_jump()

        if self.jump_start > 0:
            self.jump_start -= 1
            self.motion.y -= 3.5 * self.jump_start

        else:
            if self.is_ground:
                self.jump_count = 0

            self.motion.y += 10

        self.x = gmath.clamp(
            self.width / 2,
            self.x,
            self.game.width - self.width / 2
        )

        self.y = gmath.clamp(
            self.height / 2,
            self.y,
            self.game.height - self.height / 2
        )

        if self.y is self.game.height:
            self.motion.y = 0
