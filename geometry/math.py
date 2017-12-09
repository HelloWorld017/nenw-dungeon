import math


def clamp(min_value, value, max_value):
    return max(min_value, min(value, max_value))


def rotate(polygon, theta, origin):
    new_polygon = []
    for point in polygon:
        new_polygon.append((
            (point[0] - origin.x) * math.cos(theta) + (point[1] - origin.y) * math.sin(theta) + origin.x,
            (point[0] - origin.x) * math.sin(theta) - (point[1] - origin.y) * math.cos(theta) + origin.y
        ))

    return tuple(new_polygon)
