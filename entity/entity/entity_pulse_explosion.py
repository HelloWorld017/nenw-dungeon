import math

import pygame

from entity.entity_base import Entity
from geometry.bound_box import BoundBox
from geometry.vector2 import Vector2
from render.render import Render


class EntityPulseExplosion(Entity):
    color = (3, 169, 244)

    def __init__(self, game, x, y, max_radius=None):
        super().__init__(game, BoundBox(
            Vector2(x, y), Vector2(x, y)
        ))

        self.radius = 0
        self.radius_speed = 0

        if max_radius is None:
            max_radius = math.hypot(game.width / 2, game.height / 2)

        self.max_radius = max_radius
        self.fade_tick = 30

        self.screen = pygame.Surface((game.width, game.height))
        self.screen.set_colorkey((240, 240, 240))
        self.renderer = Render(self.screen)

    def update(self, events):
        super().update(events)

        if self.radius < self.max_radius:
            self.radius_speed += 1
            self.radius += self.radius_speed

        else:
            self.fade_tick -= 1

            if self.fade_tick < 0:
                self.set_dead()

    def render(self, render):
        self.renderer.fill((240, 240, 240))
        self.screen.set_alpha(self.fade_tick / 30 * 255)

        self.renderer.circle(self, self.radius, self.color)

        render.screen.blit(self.screen, (0, 0))

