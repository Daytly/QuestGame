from dynamicGameObject import DynamicGameObject
import pygame


class Missile(DynamicGameObject):
    def __init__(self, sheet, pos_x, pos_y, game, cols, rows, speedX, speedY, owner):
        super().__init__(sheet, pos_x, pos_y, game, cols, rows)
        self.speedX = speedX
        self.speedY = speedY
        self.owner = owner

    def move(self, *args):
        if self.check(self.coord.x + self.speedX, self.coord.y + self.speedY):
            self.coord += [self.speedX, self.speedY]
            self.rect.x += self.speedX * self.game.tile_width
            self.rect.y += self.speedY * self.game.tile_height
        else:
            self.owner.conflict(self)
