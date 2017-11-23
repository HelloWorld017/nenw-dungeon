from skill.attack.skill_d.skill_group_d import SkillGroupD
from skill.skill import Skill


class SkillD(Skill):
    def __init__(self, version, multiplier, require_score, previous):
        super().__init__("D%d" % version,
                         "플레이어가 발사하는 투사체의 데미지가 %d배 증가합니다." % multiplier,
                         require_score,
                         SkillGroupD.get_instance(),
                         previous)

        self.multiplier = multiplier

    def do_activate(self, player):
        player.bullet_multiplier = self.multiplier
