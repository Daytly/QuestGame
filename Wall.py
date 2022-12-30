import pygame
from Player import Player
from StaticGameObject import StaticGameObject


class Wall(StaticGameObject):
    def __init__(self, tile_type, pos_x, pos_y, game):
        super().__init__(tile_type, pos_x, pos_y, game)
        self.solid = False

