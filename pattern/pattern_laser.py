from entity.entity.monster.entity_laser import EntityLaser
from entity.entity.monster.entity_laser_bottom import EntityLaserBottom
from geometry.bound_box import BoundBox
from geometry.vector2 import Vector2
from pattern.pattern import Pattern
from ui.components.warning.warning_square import WarningSquare


class PatternLaser(Pattern):
    time = 180
    free = 150
    pre_activate_tick = 120
    lasers = []
    speed = None
    ui = None
    warning_mid = None
    laser_mid = None
    laser_phase = 0

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
        
        if self.tick > (self.duration / 2) - 50 and self.laser_phase == 0:
            self.laser_phase = 1
            self.warning_mid = [
                WarningSquare(self.game, BoundBox(
                    Vector2(0, self.game.height - 100),
                    Vector2(self.game.width, self.game.height)
                )).show(),
                
                WarningSquare(self.game, BoundBox(
                    Vector2(0, 0),
                    Vector2(self.game.width, 100)
                )).show()
            ]
        
        elif self.tick > (self.duration / 2) and self.laser_phase == 1:
            self.laser_phase = 2
            for warning in self.warning_mid:
                warning.hide()
            
            self.warning_mid = None
            self.laser_mid = [
                EntityLaserBottom(self.game, self.game.height - 100).spawn(),
                EntityLaserBottom(self.game, 0).spawn()
            ]
        
        elif self.tick > (self.duration / 2) + 50 and self.laser_phase == 2:
            self.laser_phase = 3
            for laser in self.laser_mid:
                laser.set_dead()
            
            self.laser_mid = None
        

    def on_deactivate(self):
        super().on_deactivate()

        for laser in self.lasers:
            laser.set_dead()

    @property
    def duration(self):
        return self.time - 30
