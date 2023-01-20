import pygame
from staticGameObject import StaticGameObject


class Floor(StaticGameObject):
    def __init__(self, sheet, pos_x, pos_y, game, cols, rows, numSprite):
        super().__init__(sheet, pos_x, pos_y, game, cols, rows)
        self.update_sprite(numSprite)
        self.solid = True
