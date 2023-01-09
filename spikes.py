from staticGameObject import StaticGameObject


class Spikes(StaticGameObject):
    def __init__(self, sheet, pos_x, pos_y, game, cols, rows):
        super().__init__(sheet, pos_x, pos_y, game, cols, rows)
        self.solid = True
        self.active = False

    def update(self, *args):
        self.update_sprite(self.cur_frame + 1)
        if 9 >= self.cur_frame >= 8:
            self.active = True
        else:
            self.active = False

    def stepOn(self, entity):
        if self.active:
            try:
                entity.murder(self)
            except AttributeError:
                return self.solid
        return self.solid

    def isActive(self):
        return self.active
