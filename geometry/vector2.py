from decorators.chain import chain
import math


class Vector2(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @chain
    def multiply(self, scala):
        self.x *= scala
        self.y *= scala

    @chain
    def subtract(self, vector):
        self.x -= vector.x
        self.y -= vector.y

    @chain
    def add(self, vector):
        self.x += vector.x
        self.y -= vector.y

    @chain
    def set_x(self, x):
        self.x = x

    @chain
    def set_y(self, y):
        self.y = y

    def distance(self, target):
        return math.sqrt((self.x - target.x) ** 2 + (self.y - target.y) ** 2)

    def clone(self):
        return Vector2(self.x, self.y)

    @property
    def pos(self):
        return self.x, self.y
