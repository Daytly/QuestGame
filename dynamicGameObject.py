import pygame
from gameObject import GameObject


class DynamicGameObject(GameObject):
    def __init__(self, tile_type, pos_x, pos_y, game):
        super().__init__(tile_type, pos_x, pos_y, game)
        self.image = game.tile_images[tile_type]
        self.coord = [pos_x, pos_y]

    def check(self, x, y):
        try:
            return self.game.level[y][x].stepOn()
        except IndexError:
            return False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
