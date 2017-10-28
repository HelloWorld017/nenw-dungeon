from pygame.locals import *


class Keys:

    KEY_JUMP = K_SPACE
    KEY_RIGHT = K_RIGHT
    KEY_LEFT = K_LEFT

    @staticmethod
    def list_keys():
        return [value for prop, value in vars(Keys).items() if prop.startswith("KEY_")]

