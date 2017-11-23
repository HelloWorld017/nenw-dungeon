from entity.monster.entity_thorn import EntityThorn
from geometry.bound_box import BoundBox
from geometry.vector2 import Vector2
from pattern.pattern import Pattern
from ui.warning.warning_square import WarningSquare


class PatternThorn(Pattern):
    speed = 20
    last_fire = 0
    fire_amount = 0
    thorn_width = 0
    thorn_height = 0
    ui_list = []
    ui_list_phase_2 = []

    phase_1_trap_list = []
    traps = []

    def on_pre_activate(self):
        super().on_pre_activate()
        self.last_fire = 0
        self.fire_amount = 0
        self.thorn_width = self.game.width / 10
        self.thorn_height = EntityThorn.height

        self.ui_list = []
        self.ui_list_phase_2 = []

        self.phase_1_trap_list = []

        for i in range(5):
            self.ui_list.append(WarningSquare(self.game, BoundBox(
                Vector2((i * 2) * self.thorn_width, 0),
                Vector2((i * 2 + 1) * self.thorn_width, self.game.height)
            )).show())

    def on_activate(self):
        for elem in self.ui_list:
            elem.hide()

        for i in range(5):
            self.ui_list_phase_2.append(WarningSquare(self.game, BoundBox(
                Vector2((i * 2 + 1) * self.thorn_width, 0),
                Vector2((i * 2 + 2) * self.thorn_width, self.game.height)
            )).show())

    def do_update(self):
        super().do_update()
        if self.fire_amount <= 10:
            if self.tick >= self.last_fire + self.fire_duration:
                self.last_fire = self.last_fire + self.fire_duration

                inverse = self.fire_amount >= 5

                if self.fire_amount == 5:
                    for elem in self.ui_list_phase_2:
                        elem.hide()

                    for elem in self.ui_list:
                        elem.show()

                auto_decay = True

                if not inverse:
                    thorn_x = (self.fire_amount * 2 + 1 / 2) * self.thorn_width
                    thorn_y = -self.thorn_height / 2
                    auto_decay = False

                else:
                    thorn_x = ((self.fire_amount - 5) * 2 + 3 / 2) * self.thorn_width
                    thorn_y = self.game.height + self.thorn_height / 2

                thorn = EntityThorn(self.game, thorn_x, thorn_y, 20, inverse)
                thorn.spawn()
                thorn.auto_decay = auto_decay

                self.traps.append(thorn)

                if not inverse:
                    self.phase_1_trap_list.append(thorn)

                self.fire_amount += 1

        elif self.fire_amount == 11:
            for trap in self.phase_1_trap_list:
                trap.motion.y = -trap.motion.y

            self.fire_amount += 1

    def on_deactivate(self):
        super().on_deactivate()
        for elem in self.ui_list:
            elem.hide()

        for trap in self.traps:
            if not trap.is_dead:
                trap.set_dead()

    @property
    def time(self):
        return self.game.height / self.speed * 3 + 1

    @property
    def duration(self):
        return self.game.height / self.speed * 5 + 1

    @property
    def fire_duration(self):
        return self.time / 15
