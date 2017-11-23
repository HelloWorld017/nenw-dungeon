from decorators.singleton import singleton
from skill.attack.skill_x import SkillX
from skill.attack.skill_x.skill_x2 import SkillX2


@singleton
class SkillX3(SkillX):
    def __init__(self):
        super().__init__(2, 0, SkillX2.get_instance())
