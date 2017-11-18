from geometry.vector2 import Vector2


class BoundBox(Vector2):
    def __init__(self, min_pos, max_pos):
        self.min = min_pos
        self.max = max_pos
        super().__init__(self.x, self.y)

    @property
    def x(self):
        return (self.min.x + self.max.x) / 2

    @x.setter
    def x(self, new):
        width = self.width

        self.min.x = new - width / 2
        self.max.x = new + width / 2

    @property
    def y(self):
        return (self.min.y + self.max.y) / 2

    @y.setter
    def y(self, new):
        height = self.height

        self.min.y = new - height / 2
        self.max.y = new + height / 2

    @property
    def width(self):
        return self.max.x - self.min.x

    @width.setter
    def width(self, new):
        x = self.x

        self.min.x = x - new / 2
        self.max.x = x + new / 2

    @property
    def height(self):
        return self.max.y - self.min.y

    @height.setter
    def height(self, new):
        y = self.y

        self.min.y = y - new / 2
        self.max.y = y + new / 2

    @property
    def rect(self):
        return self.min.x, self.min.y, self.width, self.height

    @property
    def polygon(self):
        return ((self.min.x, self.min.y), (self.min.x, self.max.y),
                (self.max.x, self.max.y), (self.max.x, self.min.y))
