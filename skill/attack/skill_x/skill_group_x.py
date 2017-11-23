from decorators.singleton import singleton
from keyboard.keys import Keys
from skill.skill_group import SkillGroup


@singleton
class SkillGroupX(SkillGroup):
    def __init__(self):
        super().__init__("X", SkillGroup.SKILL_TYPE_ATTACK, Keys.KEY_SKILL_GROUP_X)
