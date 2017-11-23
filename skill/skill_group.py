from skill.skill_manager import SkillManager


class SkillGroup(object):
    SKILL_TYPE_ATTACK = 0
    SKILL_TYPE_SURVIVAL = 1
    SKILL_TYPE_SCORING = 2

    def __init__(self, name, skill_type, shortcut):
        self.name = name
        self.shortcut = shortcut
        self.type = skill_type
        self.skills = []

        SkillManager.get_instance().register(self)

    def add_skill(self, skill):
        self.skills.append(skill)
        SkillManager.get_instance().update_skills(self)
