from dynamicGameObject import DynamicGameObject
import pygame
from missile import Missile


class DarkNinja(DynamicGameObject):
    def __init__(self, sheet, pos_x, pos_y, game, cols, rows, isVertically):
        super().__init__(sheet, pos_x, pos_y, game, cols, rows)
        self.framesAttack = self.frames[4:] if isVertically else self.frames[4:]
        self.frames = self.frames[:2] if isVertically else self.frames[2:4]
        self.speedX = 0 if isVertically else 1
        self.speedY = 1 if isVertically else 0
        self.missiles = []

    def move(self, *args):
        if self.coord.x - self.game.player.coord.x == 0:
            speedX = 0
            speedY = 1 if self.coord.y - self.game.player.coord.y <= 0 else -1
            self.missiles.append(Missile('shuriken', self.coord.x, self.coord.y,
                                         self.game, 2, 1, speedX, speedY, self))
            self.game.enemies.append(self.missiles[-1])
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

    def conflict(self, other):
        self.missiles.remove(other)
        self.game.enemies.remove(other)
