import random

import pygame
from player import Player
from staticGameObject import StaticGameObject


class Wall(StaticGameObject):
    def __init__(self, sheet, pos_x, pos_y, game, cols, rows):
        super().__init__(sheet, pos_x, pos_y, game, cols, rows)
        self.update_sprite(random.randrange(cols*rows))
        self.solid = False



