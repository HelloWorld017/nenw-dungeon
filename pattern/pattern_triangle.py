import math
import random

from entity.monster.entity_triangle import EntityTriangle
from geometry.vector2 import Vector2
from pattern.pattern import Pattern


class PatternTriangle(Pattern):
    ui = None
    max_level = 3
    level_tick = 60
    rest_tick = 10
    current_level = 1
    current_level_tick = 60
    triangles = []
    created_triangles = []

    def on_pre_activate(self):
        super().on_pre_activate()
        self.current_level = 1
        self.triangles = []
        self.triangles.append(EntityTriangle(self.game, 0, math.pi / 2,
                                             Vector2(self.game.width / 2, self.game.height / 2)).spawn())

    def on_activate(self):
        super().on_activate()

    def do_update(self):
        super().do_update()

        if self.current_level > self.max_level and self.current_level_tick >= self.level_tick:
            return

        if self.current_level_tick >= self.level_tick + self.rest_tick:
            newly_created_triangles = []
            if len(self.created_triangles) == 0:
                self.created_triangles = self.triangles

            for triangle in self.created_triangles:
                random_theta = random.randint(0, 5) / 10 * math.pi

                newly_created_triangles.append(EntityTriangle(self.game, 0, random_theta,
                                                              triangle).spawn(False))
                newly_created_triangles.append(EntityTriangle(self.game, 0, random_theta + math.pi * 2 / 3,
                                                              triangle).spawn(False))
                newly_created_triangles.append(EntityTriangle(self.game, 0, random_theta + math.pi * 4 / 3,
                                                              triangle).spawn(False))

            self.created_triangles = newly_created_triangles
            self.triangles += newly_created_triangles
            self.current_level_tick = 0
            self.current_level += 1

        elif self.current_level_tick < self.level_tick:
            for triangle in self.created_triangles:
                triangle.radius += 5
                triangle.theta += math.pi / 90
                triangle.update_position()

        self.current_level_tick += 1

    def on_deactivate(self):
        super().on_deactivate()

        for triangle in self.triangles:
            triangle.set_dead()

    @property
    def duration(self):
        return self.max_level * (self.rest_tick + self.level_tick) + self.rest_tick
