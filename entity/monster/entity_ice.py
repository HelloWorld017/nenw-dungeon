from entity.entity_player_bullet import EntityPlayerBullet
from entity.monster.entity_trap import EntityTrap


class EntityIce(EntityPlayerBullet, EntityTrap):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, (0, 184, 212))

    def update(self, events):
        super().update(events)

    def render(self, renderer):
        renderer.polygon(self.bound_model, self.color)
