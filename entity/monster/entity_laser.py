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
        color = blend(self.fade / 30, self.game.background, self.color)

        renderer.rect(self, color)

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
