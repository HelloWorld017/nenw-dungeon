from decorators.singleton import singleton
from keyboard.keys import Keys
from skill.skill_group import SkillGroup


@singleton
class SkillGroupE(SkillGroup):
    def __init__(self):
        super().__init__("E", SkillGroup.SKILL_TYPE_SURVIVAL, Keys.KEY_SKILL_GROUP_E)
