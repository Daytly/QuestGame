from staticGameObject import StaticGameObject


class Key(StaticGameObject):
    def __init__(self, tile_type, pos_x, pos_y, game):
        super().__init__(tile_type, pos_x, pos_y, game)
        self.imageUnActive = game.tile_images['empty']
        self.solid = True
        self.isActive = True

    def stepOn(self):
        if self.isActive:
            self.isActive = False
            self.image = self.imageUnActive
            return False
        self.isActive = False
        return self.solid
