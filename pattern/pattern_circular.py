from entity.monster.entity_bullet import EntityBullet
from geometry.vector2 import Vector2
from pattern.pattern import Pattern
from ui.warning_circle import WarningCircle
import math


class BulletManager:
    def __init__(self, bullet):
        self.target = None
        self.motion = Vector2(0, 0)
        self.bullet = bullet
        self.left_time = 0

    def calculate_target(self, target, time, additional_time):
        self.motion = Vector2((target.x - self.bullet.x) / time, (target.y - self.bullet.y) / time)
        self.left_time = time + additional_time

    def update(self):
        if self.left_time > 0:
            self.bullet.add(self.motion)
            self.left_time -= 1

        else:
            self.motion = Vector2(0, 0)


class PatternCircular(Pattern):
    bullet_count = 30

    initial_bullet_time = 180
    initial_radius = 500
    secondary_bullet_time = 30
    final_bullet_time = 30
    rest_time = 30

    phase = "init"
    ui = None

    bullets = []

    def on_pre_activate(self):
        super().on_pre_activate()
        self.ui = WarningCircle(self.game, Vector2(self.game.width / 2, 0), self.initial_radius).show()

        self.bullets = map(lambda i: BulletManager(EntityBullet(self.game, self.game.width / 2, 0).spawn()),
                           range(self.bullet_count))

    def on_activate(self):
        super().on_activate()
        self.ui.hide()

        angle = math.pi
        step = math.pi / self.bullet_count
        phase = "initial"

        for bullet in self.bullets:
            angle += step
            bullet.calculate_target(Vector2(math.cos(angle) * self.initial_radius,
                                            math.sin(angle) * self.initial_radius), self.initial_bullet_time, 0)

    def do_update(self):
        super().do_update()
        if self.tick > self.initial_bullet_time + self.rest_time and self.phase == "initial"

        for bullet in self.bullets:
            bullet.update()

    def on_deactivate(self):
        super().on_deactivate()

    @property
    def duration(self):
        return self.initial_bullet_time + self.secondary_bullet_time + self.final_bullet_time
