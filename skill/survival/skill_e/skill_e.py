from skill.skill import Skill
from skill.survival.skill_e.skill_group_e import SkillGroupE


class SkillE(Skill):
    def __init__(self, version, percentage, require_score, previous):
        super().__init__("E%d" % version,
                         "%d%%의 확률로 공격을 회피합니다." % percentage,
                         require_score,
                         SkillGroupE.get_instance(),
                         previous)

        self.percentage = percentage

    def do_activate(self, player):
        player.evasion_percentage = self.percentage
