from skill.attack.skill_x.skill_group_x import SkillGroupX
from skill.skill import Skill


# Press X to pay joy
class SkillX(Skill):
    def __init__(self, version, require_score, previous):
        super().__init__("X%d" % version,
                         "플레이어가 발사하는 투사체의 개수가 %d개로 증가합니다." % version,
                         require_score,
                         SkillGroupX.get_instance(),
                         previous)

        self.count = version

    def do_activate(self, player):
        player.bullet_count = self.count
