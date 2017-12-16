import math
import random

from entity.entity.monster.entity_bomb import EntityBomb
from pattern.pattern import Pattern


class PatternRain(Pattern):
    intended_duration = 600
    fire_tick = 45
    activate_fly_mode = False

    def do_update(self):
        super().do_update()

        if self.inner_tick % self.fire_tick == 0:
            x = random.randint(0, self.game.width)
            EntityBomb(self.game, x, 0).spawn().rotate(math.pi * 3 / 2)

    @property
    def duration(self):
        return self.intended_duration
