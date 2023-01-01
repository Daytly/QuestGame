class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return [self.x, self.y]

    def __iadd__(self, other):
        return Coord(self.x + other[0], self.y + other[1])