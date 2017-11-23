from decorators.singleton import singleton
from skill.attack.skill_x import SkillX


@singleton
class SkillX2(SkillX):
    def __init__(self):
        super().__init__(2, 0, None)
