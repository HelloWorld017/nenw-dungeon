import math

from entity.monster.entity_turret import EntityTurret
from pattern.pattern import Pattern


class PatternTurret(Pattern):
    ui = None
    turret_spawn_tick = 160
    turret_count = 4
    turret_speed = 10
    turret_movement_tick = None
    turrets = []

    def __init__(self, game, entity):
        self.turret_movement_tick = (game.width + game.height) / self.turret_speed
        super().__init__(game, entity)

    def on_pre_activate(self):
        super().on_pre_activate()
        self.turrets = []

    def on_activate(self):
        super().on_activate()

    def do_update(self):
        super().do_update()

        if self.tick % self.turret_spawn_tick == 0 and len(self.turrets) < self.turret_count:
            self.turrets.append(EntityTurret(self.game, self.game.width - EntityTurret.size,
                                             self.game.height - EntityTurret.size, self.entity).spawn())

        for turret in self.turrets:
            if turret.x == turret.size:
                turret.rot = math.pi / 2

                if turret.y > self.game.height:
                    turret.set_dead()

            elif turret.x == self.game.width - turret.size:
                if turret.y == turret.size:
                    turret.rot = math.pi
                else:
                    turret.rot = math.pi * (3 / 2)

            turret.move(self.turret_speed)

    def on_deactivate(self):
        super().on_deactivate()

        for turret in self.turrets:
            turret.set_dead()

    @property
    def duration(self):
        return self.turret_spawn_tick * self.turret_count + self.turret_movement_tick
