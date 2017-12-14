import pygame

import geometry.math as gmath


def blend(rate, color, background):
    # Normalize rate
    rate = gmath.clamp(0, rate, 1)
    background_rate = 1 - rate

    return (
        color[0] * rate + background[0] * background_rate,
        color[1] * rate + background[1] * background_rate,
        color[2] * rate + background[2] * background_rate
    )


def blend_image(rate, image, color_key=(240, 240, 240)):
    rate = gmath.clamp(0, rate, 1)

    surface = pygame.Surface((image.get_width(), image.get_height()))

    surface.set_colorkey(color_key)
    surface.fill(color_key)
    surface.set_alpha(rate * 255)

    surface.blit(image, (0, 0))

    return surface
