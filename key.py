from staticGameObject import StaticGameObject


class Key(StaticGameObject):
    def __init__(self, sheet, pos_x, pos_y, game, cols, rows):
        super().__init__(sheet, pos_x, pos_y, game, cols, rows)
        self.solid = True
        self.isActive = True

    def stepOn(self):
        if self.isActive:
            self.isActive = False
            self.update_sprite(1)
            return False
        self.isActive = False
        return self.solid
