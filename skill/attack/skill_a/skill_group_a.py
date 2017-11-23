from decorators.singleton import singleton
from keyboard.keys import Keys
from skill.skill_group import SkillGroup


@singleton
class SkillGroupA(SkillGroup):
    def __init__(self):
        super().__init__("A", SkillGroup.SKILL_TYPE_ATTACK, Keys.KEY_SKILL_GROUP_A)
