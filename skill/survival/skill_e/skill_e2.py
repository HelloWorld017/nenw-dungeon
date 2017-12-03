from decorators.singleton import singleton
from skill.survival.skill_e.skill_e import SkillE


@singleton
class SkillE2(SkillE):
    def __init__(self):
        super().__init__(2, 10, 25, None)
