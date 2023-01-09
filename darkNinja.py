from dynamicGameObject import DynamicGameObject
import pygame
from missile import Missile


class DarkNinja(DynamicGameObject):
    def __init__(self, sheet, pos_x, pos_y, game, cols, rows, isVertically):
        super().__init__(sheet, pos_x, pos_y, game, cols, rows, game.enemies_group)
        self.framesAttack = self.frames[4:] if isVertically else self.frames[4:]
        self.frames = self.frames[:2] if isVertically else self.frames[3:1:-1]
        self.speedX = 0 if isVertically else 1
        self.speedY = 1 if isVertically else 0
        self.missiles = []

    def move(self, *args):
        if self.coord.x - self.game.player.coord.x == 0:
            t = False  # Есть ли между врагом и иргроком препятствие
            speedX = 0
            speedY = 1 if self.coord.y - self.game.player.coord.y <= 0 else -1
            if speedY == 1:
                for y in range(self.coord.y + 1, self.game.player.coord.y):
                    if not self.check(self.coord.x, y):
                        t = True
                        break
            else:
                for y in range(self.game.player.coord.y, self.coord.y):
                    if not self.check(self.coord.x, y):
                        t = True
            if not t:
                self.missiles.append(Missile('shuriken', self.coord.x,
                                             self.coord.y,
                                             self.game, 2, 1, speedX, speedY, self, self.rect))
                self.game.enemies.append(self.missiles[-1])
                self.image = self.framesAttack[1 if speedY <= 0 else 0]
                return
        if self.coord.y - self.game.player.coord.y == 0:
            t = False
            speedX = 1 if self.coord.x - self.game.player.coord.x <= 0 else -1
            speedY = 0
            if speedX == 1:
                for x in range(self.coord.x + 1, self.game.player.coord.x):
                    if not self.check(x, self.coord.y):
                        t = True
                        break
            else:
                for x in range(self.game.player.coord.x, self.coord.x):
                    if not self.check(x, self.coord.y):
                        t = True
                        break
            if not t:
                self.missiles.append(Missile('shuriken', self.coord.x,
                                             self.coord.y,
                                             self.game, 2, 1, speedX, speedY, self, self.rect))
                self.game.enemies.append(self.missiles[-1])
                self.image = self.framesAttack[2 if speedX <= 0 else 3]
                return
        if self.check(self.coord.x + self.speedX, self.coord.y + self.speedY):
            self.coord += [self.speedX, self.speedY]
            self.rect.x += self.speedX * self.game.tile_width
            self.rect.y += self.speedY * self.game.tile_height
            self.update_sprite(self.cur_frame)
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
        other.kill()
