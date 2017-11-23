from decorators.singleton import singleton
from skill.attack.skill_d import SkillD
from skill.attack.skill_d.skill_d3 import SkillD3


@singleton
class SkillD4(SkillD):
    def __init__(self):
        super().__init__(4, 1.5, 0, SkillD3.get_instance())
