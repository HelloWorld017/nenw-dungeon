from decorators.chain import chain


class Pattern(object):
    pre_activate_tick = 60
    activate_fly_mode = True

    def __init__(self, game, entity):
        self.game = game
        self.entity = entity
        self.tick = 0
        self.inner_tick = 0

    @property
    def duration(self):
        return 0

    def on_pre_activate(self):
        pass

    def on_activate(self):
        pass

    def on_deactivate(self):
        pass

    def update(self):
        self.inner_tick += 1

        if self.inner_tick == self.pre_activate_tick:
            self.on_activate()

        if self.inner_tick >= self.pre_activate_tick:
            self.do_update()
            self.tick += 1

        if self.tick >= self.duration:
            self.deactivate()

    def do_update(self):
        pass

    @chain
    def activate(self):
        self.tick = 0
        self.game.patterns.append(self)
        if self.activate_fly_mode and (not self.entity.fly_mode):
            self.entity.set_flyable(True)

        elif (not self.activate_fly_mode) and self.entity.fly_mode:
            self.entity.set_flyable(False)

        self.on_pre_activate()

    @chain
    def deactivate(self):
        self.on_deactivate()
        self.game.patterns.remove(self)
        self.game.new_pattern()
