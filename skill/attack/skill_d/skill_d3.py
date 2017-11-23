from decorators.singleton import singleton
from skill.attack.skill_d import SkillD
from skill.attack.skill_d.skill_d2 import SkillD2


@singleton
class SkillD3(SkillD):
    def __init__(self):
        super().__init__(3, 1.3, 0, SkillD2.get_instance())
