import random

from entity.entity_fadeable import EntityFadeable
from entity.entity_trap import EntityTrap
from geometry.bound_box import BoundBox
from geometry.vector2 import Vector2
from render.blend import blend


class EntityLaser(EntityFadeable, EntityTrap):
    laser_width = 50
    color = (198, 40, 40)
    friction = 0

    def __init__(self, game, x):
        super().__init__(game, BoundBox(
            Vector2(x, 0),
            Vector2(x + self.laser_width, game.height)
        ))

    def render(self, renderer):
        original_color = self.blend_color(self.color)

        renderer.rect(self, blend(7 / 8, self.game.background, original_color))

        x = self.x
        y = 0

        for j in range(2):
            color = blend(1 / (j + 2), original_color, self.game.background)
            radius = random.randint(5, 15)

            for i in range(5):
                next_x = random.randint(int(self.min.x + radius), int(self.max.x - radius))
                if i == 4:
                    next_x = self.x

                renderer.polygon((
                    (next_x - radius, y + self.height / 5),
                    (next_x, y + self.height / 5),
                    (x, y),
                    (x - radius, y)
                ), color=color)

                x = next_x
                y += self.height / 5

    @property
    def bound_model(self):
        return self.polygon

    def attack(self, target):
        target.hurt(1)
        target.motion.y += 50
        target.motion.x += 50
