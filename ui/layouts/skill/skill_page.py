from skill.skill_manager import SkillManager
from ui.faded_element import FadedElement


class SkillPage(FadedElement):
    color_key = (240, 240, 240)

    def __init__(self, game):
        super().__init__(game, game.width / 2, game.height / 2, game.width, game.height)
        self.elements = []

        margin_top = 100
        margin_left = 100

        for skill_group in SkillManager.get_instance().skills_by_type.values():
            pass

    def do_render(self, renderer):
        for element in self.elements:
            element.do_render(renderer)
