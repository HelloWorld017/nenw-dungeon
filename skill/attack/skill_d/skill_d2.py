from decorators.singleton import singleton
from skill.attack.skill_d.skill_d import SkillD


@singleton
class SkillD2(SkillD):
    def __init__(self):
        super().__init__(2, 1.1, 0, None)
