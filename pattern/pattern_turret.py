from entity.monster.entity_turret import EntityTurret
from pattern.pattern import Pattern


class PatternTriangle(Pattern):
    ui = None
    turret_spawn_tick = 60
    turret_count = 4
    turret_speed = 10
    turret_movement_tick = None
    turrets = []

    def __init__(self, game, entity):
        self.turret_spawn_tick = (game.width + game.height) / self.turret_speed
        super().__init__(game, entity)

    def on_pre_activate(self):
        super().on_pre_activate()
        self.turrets = []

    def on_activate(self):
        super().on_activate()

    def do_update(self):
        super().do_update()

        if self.tick % self.turret_spawn_tick:
            self.turrets.append(EntityTurret(self.game, self.game.width - EntityTurret.size,
                                             self.game.height - EntityTurret.size, self.entity).spawn())

    def on_deactivate(self):
        super().on_deactivate()

        for turret in self.turrets:
            turret.set_dead()

    @property
    def duration(self):
        return self.turret_spawn_tick * self.turret_count + self.turret_movement_tick
