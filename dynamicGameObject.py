import pygame
from gameObject import GameObject
from coord import Coord


class DynamicGameObject(GameObject):
    def __init__(self, sheet, pos_x, pos_y, game, cols, rows, groups):
        super().__init__(sheet, pos_x, pos_y, game, cols, rows, groups)

    def check(self, x, y):
        try:
            return self.game.level[y][x].stepOn(self)
        except IndexError:
            return False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
