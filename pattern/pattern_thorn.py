from entity.monster.entity_thorn import EntityThorn
from geometry.bound_box import BoundBox
from geometry.vector2 import Vector2
from pattern.pattern import Pattern
from ui.warning_square import WarningSquare


class PatternThorn(Pattern):
    speed = 20
    last_fire = 0
    fire_amount = 0
    thorn_width = 0
    thorn_height = 0
    ui_list = []

    def on_pre_activate(self):
        super().on_pre_activate()
        self.last_fire = 0
        self.fire_amount = 0
        self.thorn_width = self.game.width / 10
        self.thorn_height = EntityThorn.height

        self.ui_list = []

        for i in range(5):
            self.ui_list.append(WarningSquare(self.game, BoundBox(
                Vector2((i * 2) * self.thorn_width, 0),
                Vector2((i * 2 + 1) * self.thorn_width, self.thorn_height)
            )).show())

    def do_update(self):
        super().update()
        if self.tick >= self.last_fire + self.fire_duration:
            self.last_fire = self.last_fire + self.fire_duration

            inverse = self.fire_amount >= 5

            if not inverse:
                thorn_x = (self.fire_amount * 2 + 1 / 2) * self.thorn_width
                thorn_y = -self.thorn_height / 2

            else:
                thorn_x = ((self.fire_amount - 5) * 2 + 3 / 2) * self.thorn_width
                thorn_y = self.game.height + self.thorn_height / 2

            thorn = EntityThorn(self.game, thorn_x, thorn_y, 20, inverse)
            thorn.spawn()

            self.fire_amount += 1

    @property
    def duration(self):
        return self.game.height / self.speed * 2 + 1

    @property
    def fire_duration(self):
        return self.duration / 10
