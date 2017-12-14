from decorators.alive import alive
from decorators.chain import chain
from entity.entity import Entity
from geometry.collision import test_collision


class EntityTrap(Entity):
    @alive
    def update(self, events):
        super().update(events)

        for player in self.game.players:
            if test_collision(self.bound_model, player.bound_model):
                self.attack(player)

    @alive
    @chain
    def attack(self, target):
        self.set_dead()
        target.hurt(1)
