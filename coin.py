import pygame
from staticGameObject import StaticGameObject


class Coin(StaticGameObject):
    def __init__(self, sheet, pos_x, pos_y, game, cols, rows):
        super().__init__(sheet, pos_x, pos_y, game, cols, rows)
        self.rect = self.image.get_rect().move(game.tile_width * pos_x + 8, game.tile_height * pos_y + 8)
        self.solid = True
        self.active = True

    def stepOn(self, entity):
        if self.active:
            self.active = False
            self.game.all_sprites.remove(self)
        self.active = False
        return self.solid

    def isActive(self):
        return self.active

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.isActive():
            self.update_sprite(self.cur_frame + 0.2)

