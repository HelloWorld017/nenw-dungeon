import math

from ui.element import Element


class SkillView(Element):
    skill_color = (255, 152, 0)
    background_color = (240, 240, 240)

    selected = False

    def __init__(self, game, x, y, skill):
        super().__init__(game, x, y, 100, 100)
        self.skill = skill
        self.text_rect = None
        self.text_surface_background = None
        self.text_surface_foreground = None

    def init_render(self, renderer):
        font_object = renderer.load_font()
        self.text_surface_background = renderer.get_text(self.skill.name, font_object, self.background_color)

        self.text_surface_foreground = renderer.get_text(self.skill.name, font_object, self.skill_color)

    def do_render(self, renderer):
        renderer.polygon((
            (self.x + self.width / 2, self.y),
            (self.x, self.y + self.height / 2),
            (self.x - self.width / 2, self.y),
            (self.x, self.y - self.height / 2)
        ), self.skill_color, fill=self.selected, width=5)

        foreground = self.skill_color

        if self.selected:
            foreground = self.background_color
            renderer.draw_image(self.text_surface_background, self.x, self.y)

        else:
            renderer.draw_image(self.text_surface_foreground, self.x, self.y)

        if self.skill.activated:
            renderer.polygon((
                (self.x + self.width / 2 - 5 * math.sqrt(2), self.y),
                (self.x + self.width / 2 - 5 * math.sqrt(2) - 5, self.y - 5),
                (self.x, self.y - self.height / 2 - 5 * math.sqrt(2)),
                (self.x - 5, self.y - self.height / 2 - 5 * math.sqrt(2) - 5)
            ), foreground)
