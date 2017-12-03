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
    KEY_SKILL_GROUP_E = K_e
    KEY_SKILL_GROUP_X = K_x
    KEY_SKILL_UI_UP = K_UP
    KEY_SKILL_UI_DOWN = K_DOWN
    KEY_SKILL_UI_LEFT = K_LEFT
    KEY_SKILL_UI_RIGHT = K_RIGHT

    @staticmethod
    def list_keys():
        return [value for prop, value in vars(Keys).items() if prop.startswith("KEY_")]

