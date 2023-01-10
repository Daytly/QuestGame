import pygame
from dynamicGameObject import DynamicGameObject


class Slime(DynamicGameObject):
    def __init__(self, sheet, pos_x, pos_y, game, isVertically, cols, rows):
        super().__init__(sheet, pos_x, pos_y, game, cols, rows, game.enemies_group)
        self.rect = self.image.get_rect().move(game.tile_width * pos_x + 1, game.tile_height * pos_y + 1)
        self.speedX = 1
        self.speedY = 1
        if isVertically:
            self.speedX = 0
            self.frames = self.frames[:2]
        else:
            self.speedY = 0
            self.frames = self.frames[2:]

    def move(self):
        if self.check(self.coord.x + self.speedX, self.coord.y + self.speedY):
            self.coord += [self.speedX, self.speedY]
            self.rect.x += self.speedX * self.game.tile_width
            self.rect.y += self.speedY * self.game.tile_height
        else:
            self.speedY *= -1
            self.speedX *= -1
            self.update_sprite((self.cur_frame + 1) % 2)
            self.coord += [self.speedX, self.speedY]
            self.rect.x += self.speedX * self.game.tile_width
            self.rect.y += self.speedY * self.game.tile_height
