import pygame
from staticGameObject import StaticGameObject


class Star(StaticGameObject):
    def __init__(self, sheet, pos_x, pos_y, game, cols, rows):
        super().__init__(sheet, pos_x, pos_y, game, cols, rows)



