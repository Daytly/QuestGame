from dynamicGameObject import DynamicGameObject
import pygame


class DarkNinja(DynamicGameObject):
    def __init__(self, sheet, pos_x, pos_y, game, cols, rows, isVertically):
        super().__init__(sheet, pos_x, pos_y, game, cols, rows)
        self.framesAttack = self.frames[4:] if isVertically else self.frames[4:]
        self.frames = self.frames[:2] if isVertically else self.frames[2:4]
        self.speedX = 0 if isVertically else 1
        self.speedY = 1 if isVertically else 0
        self.missiles = []

    def update(self, *args):
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
