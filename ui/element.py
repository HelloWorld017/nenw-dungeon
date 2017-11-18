from decorators.chain import chain


class Element(object):
    is_pre = False

    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y

    def render(self, renderer):
        pass

    @chain
    def hide(self):
        if self.is_pre:
            self.game.pre_ui.remove(self)

        else:
            self.game.ui.remove(self)

    @chain
    def show(self):
        if self.is_pre:
            self.game.pre_ui.append(self)

        else:
            self.game.ui.append(self)