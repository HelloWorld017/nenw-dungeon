import random

from entity.monster.entity_trap import EntityTrap
from geometry.bound_box import BoundBox
from geometry.vector2 import Vector2
from render.blend_color import blend


class EntityLaser(EntityTrap):
    laser_width = 50
    color = (198, 40, 40)
    friction = 0
    fade = 0
    fade_direction = 1

    def __init__(self, game, x):
        super().__init__(game, BoundBox(
            Vector2(x, 0),
            Vector2(x + self.laser_width, game.height)
        ))

        self.on_fade_end = lambda: None

    def update(self, events):
        super().update(events)

        if 0 < self.fade < 30:
            self.fade -= self.fade_direction

            if self.fade == 0 or self.fade == 30:
                self.on_fade_end()

    def render(self, renderer):
        original_color = blend(self.fade / 30, self.game.background, self.color)

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

    def spawn(self):
        super().spawn()
        self.fade = 29

    def set_dead(self):
        self.fade = 1
        self.fade_direction = -self.fade_direction

        laser_super = super()

        self.on_fade_end = lambda: laser_super.set_dead()
