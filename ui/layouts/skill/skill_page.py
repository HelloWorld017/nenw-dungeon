from decorators.propagate_event import propagate_event
from skill.skill_manager import SkillManager
from ui.components.carousel import Carousel
from ui.components.label import Label
from ui.faded_element import FadedElement
from ui.layouts.skill.skill_group import SkillGroup as SkillGroupElement
from ui.layouts.skill.skill_view import SkillView


@propagate_event
class SkillPage(FadedElement):
    color_key = (240, 240, 240)
    ui_event = True

    def __init__(self, game):
        super().__init__(game, game.width / 2, game.height / 2, game.width, game.height)
        self.elements = []

        margin_top = 100
        margin_left = 100

        carousel_width = SkillView.width * 3 + SkillGroupElement.gap * 2

        group_elements = []

        for skill_group in SkillManager.get_instance().groups.values():
            group = SkillGroupElement(game, margin_left, 0, skill_group)
            group_elements.append(group)

        self.elements.append(Carousel(
            game, margin_left, margin_top + game.height / 5,
            carousel_width, SkillView.height, group_elements
        ))

        self.elements.append(Label(self.game, margin_left, margin_top, 125, 30, "Skill", 25))

    def do_render(self, renderer):
        for element in self.elements:
            element.render(renderer)
