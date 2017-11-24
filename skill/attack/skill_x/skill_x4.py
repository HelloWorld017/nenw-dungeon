from decorators.singleton import singleton
from skill.attack.skill_x.skill_x import SkillX
from skill.attack.skill_x.skill_x3 import SkillX3


@singleton
class SkillX4(SkillX):
    def __init__(self):
        super().__init__(4, 50, SkillX3.get_instance())
