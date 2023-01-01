import pygame
from dynamicGameObject import DynamicGameObject


class Slime(DynamicGameObject):
    def __init__(self, tile_type, pos_x, pos_y, game, isVertically):
        super().__init__(tile_type, pos_x, pos_y, game)
        self.speedX = 1
        self.speedY = 1
        if isVertically:
            self.speedX = 0
        else:
            self.speedY = o

    def update(self, *args):
        if self.check(self.coord)
        self.rect.x -= 50
        self.coord[0] -= 1
