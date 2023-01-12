class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return [self.x, self.y]

    def __iadd__(self, other):
        return Coord(self.x + other[0], self.y + other[1])

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f'{self.x} {self.y}'

    def __copy__(self):
        return Coord(self.x, self.y)
