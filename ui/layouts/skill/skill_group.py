from decorators.propagate_event import propagate_event
from ui.faded_element import FadedElement
from ui.layouts.skill.skill_view import SkillView


@propagate_event
class SkillGroup(FadedElement):
    color_key = (240, 240, 240)
    gap = 20
    fade_use_left_top = True
    activated = False

    def __init__(self, game, x, y, group, parent):
        super().__init__(game, x, y, SkillView.width * len(group.skills) + self.gap * (len(group.skills) + 3),
                         SkillView.height + self.gap)

        self.elements = []
        self.group = group
        self.parent = parent

        for index, skill in enumerate(group.skills):
            start_x = (index - 1) * (SkillView.width + self.gap)
            self.elements.append(SkillView(
                game,
                self.x + start_x + SkillView.width / 2,
                self.y + SkillView.height / 2 + self.gap / 2,
                skill,
                self))

    @property
    def selected_skill(self):
        if not self.activated:
            return None

        if self.parent.selected_index >= len(self.group.skills):
            self.parent.selected_index = len(self.group.skills) - 1

        return self.group.skills[self.parent.selected_index].name

    @property
    def length(self):
        return len(self.group.skills)

    def do_render(self, renderer):
        super().do_render(renderer)

        for elem in self.elements:
            elem.render(renderer)
