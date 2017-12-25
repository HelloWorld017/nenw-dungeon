from ui.components.label import Label


class Score(Label):
    def __init__(self, game, player):
        super().__init__(game, 50, 120, 400, 200, "점수: ", 32, (0, 150, 136))
        self.player = player

    def do_render(self, renderer):
        self.text = "점수: %d" % self.player.score
        self.text_image = renderer.get_text(self.text, self.font, self.color)

        renderer.screen.blit(self.text_image, (0, 0))
