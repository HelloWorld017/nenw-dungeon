import random
import math

import pygame

from decorators.delay import delay
from entity.entity.entity_health_pack import EntityHealthPack
from entity.entity.entity_pulse_explosion import EntityPulseExplosion
from entity.entity.monster.entity_mimic import EntityMimic
from pattern.pattern import Pattern
from ui.components.blink_image import BlinkImage


class PatternFakey(Pattern):
    time = 400
    downfall_tick = 400
    after_tick = 200
    spawn_count = 20
    true_count = 5
    explosion = None
    blink = None

    def __init__(self, game, entity):
        super().__init__(game, entity)
        self.spawn_map = [False] * self.spawn_count
        self.spawn_tick = math.floor(self.time / (self.spawn_count + self.true_count))

        for i in range(self.true_count):
            random_index = random.randint(0, len(self.spawn_map))
            self.spawn_map.insert(random_index, True)

        self.image = None
        self.load_image()

    # noinspection PyUnresolvedReferences
    def load_image(self):
        self.image = pygame.image.load("./resources/hp-2.png")

    def do_update(self):
        super().do_update()

        if self.tick < self.time + self.downfall_tick:
            if self.tick % self.spawn_tick == 0:
                current_index = int(math.floor(self.tick / self.spawn_tick))

                if len(self.spawn_map) <= current_index:
                    return

                if self.spawn_map[current_index]:
                    cls = EntityHealthPack

                else:
                    cls = EntityMimic

                x = random.randint(0, self.game.width)
                y = -30

                entity = cls(self.game, x, y)
                entity.motion.y = 2.2
                entity.spawn()

        elif self.tick == self.time + self.downfall_tick:
            self.explosion = EntityPulseExplosion(self.game, self.game.width / 2, self.game.height / 2).spawn()
            self.blink = BlinkImage(self.game, self.game.width / 2, self.game.height / 2, self.image).show()
            self.entity.hurt(2)

            @delay(2.5)
            def turn_off():
                self.blink.hide()

            turn_off()

        else:
            player_delta_x = (self.game.width / 2 - self.entity.x) / 5
            player_delta_y = (self.game.height / 2 - self.entity.y) / 5

            self.entity.x += player_delta_x
            self.entity.y += player_delta_y

    def on_deactivate(self):
        super().on_deactivate()

    @property
    def duration(self):
        return self.time + self.after_tick + self.downfall_tick
