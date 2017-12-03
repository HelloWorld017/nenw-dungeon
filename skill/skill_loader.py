from skill.attack.skill_a.skill_a import SkillA
from skill.attack.skill_d.skill_d2 import SkillD2
from skill.attack.skill_d.skill_d3 import SkillD3
from skill.attack.skill_d.skill_d4 import SkillD4
from skill.attack.skill_x.skill_x2 import SkillX2
from skill.attack.skill_x.skill_x3 import SkillX3
from skill.attack.skill_x.skill_x4 import SkillX4
from skill.survival.skill_e.skill_e2 import SkillE2


def register_all_skills():
    SkillD2.get_instance()
    SkillD3.get_instance()
    SkillD4.get_instance()

    SkillX2.get_instance()
    SkillX3.get_instance()
    SkillX4.get_instance()

    SkillA.get_instance()

    SkillE2.get_instance()
