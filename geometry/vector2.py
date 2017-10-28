class Vector2(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def multiply(self, scala):
        self.x *= scala
        self.y *= scala

    def subtract(self, vector):
        self.x -= vector.x
        self.y -= vector.y

    def add(self, vector):
        self.x += vector.x
        self.y -= vector.y

    @property
    def pos(self):
        return self.x, self.y
