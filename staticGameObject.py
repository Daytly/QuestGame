import pygame
from gameObject import GameObject
from coord import Coord


class StaticGameObject(GameObject):
    def __init__(self, sheet, pos_x, pos_y, game, cols, rows):
        super().__init__(sheet, pos_x, pos_y, game, cols, rows, ())
        self.solid = True

    def stepOn(self, entity):
        return self.solid
