from skill.attack.skill_a.skill_group_a import SkillGroupA
from skill.skill import Skill


class SkillA(Skill):
    def __init__(self):
        super().__init__("A",
                         "발사각도가 자동으로 몬스터를 향해 조절됩니다.",
                         50,
                         SkillGroupA.get_instance(),
                         None)

    def do_activate(self, player):
        player.aim_auto = True
