import math
import pygame

from decorators.alive import alive
from decorators.chain import chain
from entity.entity_living import EntityLiving
from entity.entity_player_bullet import EntityPlayerBullet
from geometry.bound_box import BoundBox
from geometry.vector2 import Vector2
import geometry.math as gmath
from keyboard.keys import Keys
import pygame.locals as pg_vars
from ui.components.aim_indicator import AimIndicator
from ui.components.health_bar import HealthBar


class Player(EntityLiving):
    friction = 0.7
    air_jump = False
    jump_start = 0
    jump_count = 0
    health = 5
    max_health = 5
    max_hurt_animate_tick = 30

    # Firing
    aim = 0
    aim_auto = False
    bullet_multiplier = 1.0
    bullet_count = 1
    bullet_color = (206, 147, 216)
    fire_tick = 10
    last_fire_tick = 0

    evasion_percentage = 0

    def __init__(self, game):
        super().__init__(game, BoundBox(
            Vector2(game.width / 2 - 25, game.height - 50),
            Vector2(game.width / 2 + 25, game.height)
        ))

        self.hurt_animate_tick = 0
        self.point = 0
        self.score = 0

    def spawn(self):
        super().spawn()
        self.game.players.append(self)
        HealthBar(self.game, 50, 50, self).show()
        AimIndicator(self.game, self).show()

    def set_dead(self):
        super().set_dead()
        self.game.players.remove(self)

    def render(self, renderer):
        super().render(renderer)
        hurt_amount = 1 - (abs(self.hurt_animate_tick - self.max_hurt_animate_tick / 2)
                           / (self.max_hurt_animate_tick / 2))

        renderer.rect(self, (220, 200 - hurt_amount * 100, 80))

    def do_jump(self):
        if self.air_jump and self.is_ground:
            return

        if self.jump_count >= 2:
            return

        self.jump_start = 10
        self.jump_count += 1

    @property
    def is_ground(self):
        return self.max.y >= self.game.height

    def hurt(self, hurt_amount):
        super().hurt(hurt_amount)

        self.motion.y += -50
        self.hurt_animate_tick = self.max_hurt_animate_tick

    @alive
    @chain
    def teleport(self, x, y, rotation=None):
        delta_x = x - self.x
        self.aim += delta_x

        super().teleport(x, y, rotation)

    def update(self, events):
        super().update(events)
        if self.game.key_maps[Keys.KEY_LEFT]:
            self.rotate(math.pi)
            self.move(15)

        if self.game.key_maps[Keys.KEY_RIGHT]:
            self.rotate(0)
            self.move(15)

        bullet_angle = 0

        if self.game.key_maps[Keys.KEY_AIM_LEFT]:
            self.aim = self.x - (1 / math.tan(math.pi / 3)) * self.y
            bullet_angle = math.pi / 6

        elif self.game.key_maps[Keys.KEY_AIM_RIGHT]:
            self.aim = self.x + (1 / math.tan(math.pi / 3)) * self.y
            bullet_angle = -math.pi / 6

        else:
            self.aim = self.x

        if self.game.tick > self.last_fire_tick + self.fire_tick and pygame.key.get_mods() & Keys.KEY_FIRE:
            self.last_fire_tick = self.game.tick
            bullet = EntityPlayerBullet(self.game, self.x, self.y, self.bullet_color).spawn()
            bullet.rotate(bullet_angle)

        for event in events:
            if event.type is pg_vars.KEYDOWN:
                if event.key is Keys.KEY_JUMP:
                    self.do_jump()

        if self.jump_start > 0:
            self.jump_start -= 1
            self.motion.y -= 3.5 * self.jump_start

        else:
            if self.is_ground:
                self.jump_count = 0

            self.motion.y += 10

        self.x = gmath.clamp(
            self.width / 2,
            self.x,
            self.game.width - self.width / 2
        )

        self.y = gmath.clamp(
            self.height / 2,
            self.y,
            self.game.height - self.height / 2
        )

        if self.y is self.game.height:
            self.motion.y = 0

        if self.hurt_animate_tick > 0:
            self.hurt_animate_tick -= 1
