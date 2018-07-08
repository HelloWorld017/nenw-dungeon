import random

from entity.entity_fadeable import EntityFadeable
from entity.entity_trap import EntityTrap
from geometry.bound_box import BoundBox
from geometry.vector2 import Vector2
from render.blend import blend


class EntityLaserBottom(EntityFadeable, EntityTrap):
    laser_height = 100
    color = (198, 40, 40)
    friction = 0

    def __init__(self, game, y):
        super().__init__(game, BoundBox(
            Vector2(0, y),
            Vector2(game.width, y + self.laser_height)
        ))

    def render(self, renderer):
        original_color = self.blend_color(self.color)

        renderer.rect(self, blend(7 / 8, self.game.background, original_color))

        x = 0
        y = self.y

        for j in range(2):
            color = blend(1 / (j + 2), original_color, self.game.background)
            radius = random.randint(5, 15)

            for i in range(5):
                next_y = random.randint(int(self.min.y + radius), int(self.max.y - radius))
                if i == 4:
                    next_y = self.y

                renderer.polygon((
                    (x + self.width / 5, next_y - radius),
                    (x + self.width / 5, next_y),
                    (x, y),
                    (x, y - radius)
                ), color=color)
    
                x += self.width / 5
                y = next_y

    @property
    def bound_model(self):
        return self.polygon

    def attack(self, target):
        target.hurt(1)
        
        if self.y >= self.game.height / 2:
            target.motion.y -= 50
        
        else:
            target.motion.y += 50
