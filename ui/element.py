from decorators.chain import chain


class Element(object):
    is_pre = False

    def __init__(self, game, x, y, width, height):
        self.game = game
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.is_hidden = True
        self.tick = 0

    def render(self, renderer):
        if self.tick == 1:
            self.init_render(renderer)

        self.tick += 1
        self.do_render(renderer)

    def init_render(self, renderer):
        pass

    def do_render(self, renderer):
        pass

    @chain
    def hide(self):
        if self.is_hidden:
            return

        self.is_hidden = True

        if self.is_pre:
            self.game.pre_ui.remove(self)

        else:
            self.game.ui.remove(self)

    @chain
    def show(self):
        if not self.is_hidden:
            return

        self.is_hidden = False

        if self.is_pre:
            self.game.pre_ui.append(self)

        else:
            self.game.ui.append(self)
