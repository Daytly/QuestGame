import pygame

from staticGameObject import StaticGameObject
import mixer as mx


class Key(StaticGameObject):
    def __init__(self, sheet, pos_x, pos_y, game, cols, rows):
        super().__init__(sheet, pos_x, pos_y, game, cols, rows)
        r = pygame.Rect(game.tile_width * pos_x + 1, game.tile_height * pos_y + 1, 48, 48)
        self.rect = self.image.get_rect()
        self.rect.center = r.center
        self.solid = True
        self.isActive = True

    def stepOn(self, entity):
        if self.isActive:
            mx.mixer.play('coin', loops=0)
            self.game.player.pick_up_key()
            self.isActive = False
            self.kill()
        return self.solid

    def use(self):
        if self.isActive:
            self.game.player.pick_up_key()