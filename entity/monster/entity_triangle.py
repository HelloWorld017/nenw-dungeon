import math
import geometry.math as gmath
from entity.entity_fadeable import EntityFadeable

from entity.monster.entity_trap import EntityTrap
from geometry.bound_box import BoundBox
from geometry.vector2 import Vector2


class EntityTriangle(EntityTrap, EntityFadeable):
    color = (144, 202, 249)
    size = 50

    def __init__(self, game, r, theta, origin):
        super().__init__(game, BoundBox(Vector2(0, 0), Vector2(0, 0)))
        self.radius = r
        self.theta = theta
        self.origin = origin
        self.triangle_polygon = None
        self.update_position()

        x_map = list(map(lambda pos: pos[0], self.polygon))
        y_map = list(map(lambda pos: pos[1], self.polygon))

        self.width = max(x_map) - min(x_map)
        self.height = max(y_map) - min(y_map)

    def get_polygon(self):
        # self position is center point
        return gmath.rotate((
            (self.x, self.y - self.size),
            (self.x + math.cos(math.pi / 6) * self.size, self.y + math.sin(math.pi / 6) * self.size),
            (self.x - math.cos(math.pi / 6) * self.size, self.y + math.sin(math.pi / 6) * self.size)
        ), self.theta + math.pi / 2, self)

    @property
    def polygon(self):
        return self.triangle_polygon

    def update_position(self):
        self.x = self.origin.x + math.cos(self.theta) * self.radius
        self.y = self.origin.y - math.sin(self.theta) * self.radius
        self.triangle_polygon = self.get_polygon()

    def render(self, renderer):
        renderer.polygon(self.polygon, self.blend_color(self.color))

