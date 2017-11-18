from functools import reduce
import math


def get_axis(polygon):
    sides = []

    def get_side(p1, p2):
        angle = math.atan2(p1[0] - p2[0], p1[1] - p2[1])
        sides.append(angle)
        sides.append(angle + math.pi / 2)
        return p2

    reduce(get_side, polygon, polygon[-1])

    return sides


def test_collision(o1, o2):
    axes = get_axis(o1) + get_axis(o2)
    collides = True

    for axis in axes:

        def convert_axis(point):
            point_atan = math.atan2(point[0], point[1])

            return math.cos(axis - point_atan) * math.sqrt(point[0] ** 2 + point[1] ** 2)

        o1_points = list(map(convert_axis, o1))
        o2_points = list(map(convert_axis, o2))

        if not(min(o1_points) < max(o2_points) and min(o2_points) < max(o1_points)):
            collides = False

    return collides
