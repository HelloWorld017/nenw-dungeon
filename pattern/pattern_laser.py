from entity.monster.entity_laser import EntityLaser
from geometry.bound_box import BoundBox
from geometry.vector2 import Vector2
from pattern.pattern import Pattern
from ui.warning.warning_square import WarningSquare


class PatternLaser(Pattern):
    time = 180
    free = 150
    lasers = []
    speed = None
    ui = None

    def on_pre_activate(self):
        super().on_pre_activate()
        self.speed = (self.game.width - self.free) / self.time

        laser_width = EntityLaser.laser_width
        player_width = self.entity.width

        self.lasers = [
            EntityLaser(self.game, 5 - laser_width),
            EntityLaser(self.game, 5 + player_width + self.free)
        ]

        self.ui = [
            WarningSquare(self.game, BoundBox(
                Vector2(0, 0),
                Vector2(5, self.game.height)
            )).show(),

            WarningSquare(self.game, BoundBox(
                Vector2(5 + player_width + self.free, 0),
                Vector2(5 + player_width + self.free + laser_width, self.game.height)
            )).show()
        ]

    def on_activate(self):
        super().on_activate()

        for ui in self.ui:
            ui.hide()

        for laser in self.lasers:
            laser.spawn()
            laser.motion.x = self.speed

    def do_update(self):
        super().do_update()

    def on_deactivate(self):
        super().on_deactivate()

        for laser in self.lasers:
            laser.set_dead()

    @property
    def duration(self):
        return self.time - 30
