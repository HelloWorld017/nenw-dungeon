import math
import random


from entity.monster.entity_bullet import EntityBullet
from geometry.bound_box import BoundBox
from geometry.vector2 import Vector2
from pattern.pattern import Pattern
from ui.components.warning.warning_circle import WarningCircle
from ui.components.warning.warning_square import WarningSquare


class BulletManager:
    def __init__(self, bullet):
        self.target = None
        self.motion = Vector2(0, 0)
        self.bullet = bullet
        self.left_time = 0
        self.callback_called = False

    def callback(self):
        pass

    def calculate_target(self, target, time, additional_time):
        self.left_time = time + additional_time
        self.motion = Vector2((target.x - self.bullet.x) / time, (target.y - self.bullet.y) / time)
        self.callback_called = False

    def update(self):
        if self.left_time > 0:
            self.bullet.add(self.motion)
            self.left_time -= 1

        else:
            self.motion = Vector2(0, 0)

            if not self.callback_called:
                self.callback()
                self.callback_called = True


class PatternCircular(Pattern):
    bullet_count = 30

    initial_bullet_time = 120
    initial_radius = 500
    secondary_bullet_time = 15
    third_bullet_time = 120
    final_bullet_time = 15
    over_bullet_time = 1
    rest_time = 45

    phase = "init"
    ui = None

    bullets = []
    pos_save = None

    def on_pre_activate(self):
        super().on_pre_activate()
        self.ui = WarningCircle(self.game, Vector2(self.game.width / 2, 0), self.initial_radius).show()

        self.bullets = list(map(lambda i: BulletManager(EntityBullet(self.game, self.game.width / 2, 0).spawn()),
                                range(self.bullet_count)))

    def on_activate(self):
        super().on_activate()
        self.ui.hide()

        angle = math.pi
        step = math.pi / self.bullet_count
        self.phase = "initial"

        for bullet in self.bullets:
            angle += step
            bullet.calculate_target(Vector2(self.game.width / 2 + math.cos(angle) * self.initial_radius,
                                            -math.sin(angle) * self.initial_radius), self.initial_bullet_time, 0)

    def do_update(self):
        super().do_update()
        for bullet in self.bullets:
            bullet.update()

        if self.tick > self.initial_bullet_time and self.phase == "initial":
            self.phase = "first_attack_warn"
            self.ui = WarningCircle(self.game, self.entity, self.entity.width).show()
            self.pos_save = self.entity.clone()

        if self.tick > self.initial_bullet_time + self.rest_time and self.phase == "first_attack_warn":
            self.phase = "first_attack"
            self.ui.hide()
            for bullet in self.bullets:
                bullet.calculate_target(self.pos_save, self.secondary_bullet_time, self.over_bullet_time)

        if self.tick > (self.initial_bullet_time + self.secondary_bullet_time + self.over_bullet_time +
                        self.rest_time) and self.phase == "first_attack":

            self.phase = "second_attack_warn"
            self.ui = WarningSquare(self.game, BoundBox(Vector2(0, 0), Vector2(self.game.width, self.game.height)))\
                .show()

        if self.tick > (self.initial_bullet_time + self.secondary_bullet_time + self.over_bullet_time +
                        self.rest_time * 2) and self.phase == "second_attack_warn":

            bullet_min = 0
            bullet_max = self.game.width / 2

            if self.entity.x > self.game.width / 2:
                bullet_min = bullet_max
                bullet_max = self.game.width

            for bullet in self.bullets:
                x = random.randint(bullet_min, bullet_max)

                if random.randint(0, 10) >= 8:
                    x = random.randint(self.game.width - bullet_max, self.game.width - bullet_min)

                bullet.calculate_target(Vector2(x, random.randint(0, self.game.height)), self.third_bullet_time, 0)

            self.phase = "second_attack"
            self.ui.hide()

        if self.tick > (self.initial_bullet_time + self.secondary_bullet_time + self.over_bullet_time +
                        self.third_bullet_time + self.rest_time * 2) and self.phase == "second_attack":

            self.phase = "third_attack_warn"
            self.ui = WarningCircle(self.game, self.entity, self.entity.width).show()
            self.pos_save = self.entity.clone()

        if self.tick > (self.initial_bullet_time + self.secondary_bullet_time + self.over_bullet_time +
                        self.third_bullet_time + self.rest_time * 3) and self.phase == "third_attack_warn":

            self.phase = "third_attack"
            self.ui.hide()
            for bullet in self.bullets:
                bullet.calculate_target(self.pos_save, self.final_bullet_time, self.over_bullet_time)

    def on_deactivate(self):
        super().on_deactivate()
        for bullet in self.bullets:
            bullet.bullet.set_dead()

    @property
    def duration(self):
        return self.initial_bullet_time + self.secondary_bullet_time + self.third_bullet_time + \
               self.final_bullet_time + self.over_bullet_time * 2 + self.rest_time * 3
