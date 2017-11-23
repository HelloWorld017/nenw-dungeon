from decorators.singleton import singleton
from keyboard.keys import Keys
from skill.skill_group import SkillGroup


@singleton
class SkillGroupD(SkillGroup):
    def __init__(self):
        super().__init__("D", SkillGroup.SKILL_TYPE_ATTACK, Keys.KEY_SKILL_GROUP_D)
