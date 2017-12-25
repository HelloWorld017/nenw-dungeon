import random

from entity.entity.monster.entity_dropper import EntityDropper
from geometry.bound_box import BoundBox
import geometry.math as gmath
from geometry.vector2 import Vector2
from pattern.pattern import Pattern
from ui.components.warning.warning_square import WarningSquare


class PatternDrop(Pattern):
    drop_tick = 60
    random_plus = 0
    pulse_count = 5
    pulse_interval = 120
    ui = None
    mobs = []
    activate_fly_mode = False

    def __init__(self, game, entity):
        super().__init__(game, entity)
        self.dropper_x = entity.x
        self.dropper_motion_x = 0
        self.random_plus = random.randint(0, 60)

    def on_pre_activate(self):
        super().on_pre_activate()
        self.ui = WarningSquare(self.game, BoundBox(
            Vector2(self.dropper_x - 40, self.game.height - 120),
            Vector2(self.dropper_x + 40, self.game.height),
        )).show()

    def update(self):
        super().update()
        self.dropper_motion_x += (self.entity.x - self.dropper_x) / 200
        self.dropper_x += self.dropper_motion_x
        self.dropper_x = gmath.clamp(0, self.dropper_x, self.game.width)
        self.ui.bound_box.x = self.dropper_x

    def do_update(self):
        super().do_update()

        if (self.tick == self.random_plus) or (self.tick > 3 * self.random_plus and not self.ui.is_hidden):
            mob = EntityDropper(self.game, self.dropper_x, -30).fade_spawn(animate=False)
            mob.motion.set_y(100)
            self.mobs.append(mob)
            if self.tick > 3 * self.random_plus:
                self.ui.hide()

        if self.tick > self.random_plus and self.tick % self.pulse_interval == 0:
            for mob in self.mobs:
                left_mob = EntityDropper(self.game, mob.x, mob.y).fade_spawn(animate=False)
                right_mob = EntityDropper(self.game, mob.x, mob.y).fade_spawn(animate=False)

                speed = max((mob.x + 30, self.game.width - mob.x + 30)) / 25

                left_mob.fade_set_dead(animate=True).motion.set_x(-speed)
                right_mob.fade_set_dead(animate=True).motion.set_x(speed)

    def on_deactivate(self):
        super().on_deactivate()
        for mob in self.mobs:
            mob.fade_set_dead(animate=True)

    @property
    def duration(self):
        return self.pulse_count * self.pulse_interval + self.drop_tick + self.random_plus
