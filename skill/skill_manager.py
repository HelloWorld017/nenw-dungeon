from decorators.singleton import singleton


@singleton
class SkillManager(object):
    groups = {}
    skills = {}
    skills_by_type = {}

    def register(self, group):
        if group.type not in self.skills:
            self.skills_by_type[group.type] = {}

        self.skills_by_type[group.type][group.name] = group
        self.groups[group.name] = group
        self.update_skills(group)

    def update_skills(self, group):
        for skill in group.skills:
            if skill.name not in self.skills:
                self.skills[skill.name] = skill
