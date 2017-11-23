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

    def render(self, renderer):
        self.do_render(renderer)

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
