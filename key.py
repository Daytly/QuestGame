from staticGameObject import StaticGameObject


class Key(StaticGameObject):
    def __init__(self, tile_type, pos_x, pos_y, game):
        super().__init__(tile_type, pos_x, pos_y, game)
        self.solid = True

    def stepOn(self):
        return self.solid
