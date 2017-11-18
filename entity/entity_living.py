from decorators.alive import alive
from decorators.chain import chain
from entity.entity import Entity


class EntityLiving(Entity):
    health = 10
    max_health = 10
    max_invincible_time = 15

    def __init__(self, game, bound_box):
        super().__init__(game, bound_box)
        self.invincible_time = 0

    @alive
    @chain
    def set_health(self, health):
        self.health = max(0, min(self.max_health, health))

        if self.health == 0:
            self.set_dead()

    @chain
    def set_max_health(self, max_health):
        self.max_health = max_health

    @alive
    @chain
    def heal(self, heal_amount):
        heal_amount = max(0, heal_amount)
        self.set_health(self.health + heal_amount)

    @alive
    @chain
    def hurt(self, hurt_amount):
        if self.invincible_time > 0:
            return

        hurt_amount = max(0, hurt_amount)
        self.set_health(self.health - hurt_amount)
        self.invincible_time = self.max_invincible_time

    @alive
    def update(self, events):
        super().update(events)

        if self.invincible_time > 0:
            self.invincible_time -= 1