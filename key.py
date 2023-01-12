from staticGameObject import StaticGameObject
import mixer as mx


class Key(StaticGameObject):
    def __init__(self, sheet, pos_x, pos_y, game, cols, rows):
        super().__init__(sheet, pos_x, pos_y, game, cols, rows)
        self.rect = self.image.get_rect().move(game.tile_width * pos_x + 1, game.tile_height * pos_y + 1)
        self.solid = True
        self.isActive = True

    def stepOn(self, entity):
        if self.isActive:
            mx.mixer.play('openDoor', loops=0)
            self.isActive = False
            self.update_sprite(1)
        self.isActive = False
        return self.solid
