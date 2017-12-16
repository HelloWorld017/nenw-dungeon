from decorators.chain import chain
from entity.entity_living import EntityLiving
from entity.entity_trap import EntityTrap


class EntityMob(EntityLiving, EntityTrap):
    @chain
    def spawn(self):
        super().spawn()
        self.game.mobs.append(self)
