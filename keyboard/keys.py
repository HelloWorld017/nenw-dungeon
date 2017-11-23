from pygame.locals import *


class Keys:

    KEY_JUMP = K_SPACE
    KEY_LEFT = K_LEFT
    KEY_RIGHT = K_RIGHT
    KEY_AIM_LEFT = K_a
    KEY_AIM_RIGHT = K_d
    KEY_FIRE = KMOD_CTRL
    KEY_SKILL_GROUP_A = K_a
    KEY_SKILL_GROUP_D = K_d
    KEY_SKILL_GROUP_X = K_x

    @staticmethod
    def list_keys():
        return [value for prop, value in vars(Keys).items() if prop.startswith("KEY_")]

