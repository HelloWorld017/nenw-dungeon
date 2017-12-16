from decorators.alive import alive
from decorators.chain import chain
from entity.entity_base import Entity
from render.blend import blend


class EntityFadeable(Entity):

    is_dead_anim_in_progress = False

    def __init__(self, game, bound_box):
        super().__init__(game, bound_box)

        self.fade_tick = 0
        self.fade_direction = 1
        self.on_fade_end = lambda: None

    def update(self, events):
        super().update(events)
        if 30 > self.fade_tick > 0:
            self.fade_tick += self.fade_direction

            if self.fade_tick == 0 or self.fade_tick == 30:
                self.fade_direction = 0
                self.on_fade_end()

    @chain
    def spawn(self):
        self.fade_spawn()

    @chain
    def fade_spawn(self, animate=True):
        super().spawn()
        if animate:
            self.fade_tick = 29
            self.fade_direction = -1

    @alive
    @chain
    def set_dead(self):
        self.fade_set_dead()

    @alive
    @chain
    def fade_set_dead(self, animate=True):
        if self.is_dead_anim_in_progress:
            return

        self.is_dead_anim_in_progress = True

        if not animate:
            super().set_dead()
            return

        self.fade_tick = 1
        self.fade_direction = 1

        laser_super = super()

        self.on_fade_end = lambda: laser_super.set_dead()

    def blend_color(self, color):
        return blend(self.fade_tick / 30, self.game.background, color)
