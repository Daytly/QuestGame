from dynamicGameObject import DynamicGameObject
import pygame
from coord import Coord


class Missile(DynamicGameObject):
    def __init__(self, sheet, pos_x, pos_y, game, cols, rows, speedX, speedY, owner, rect):
        super().__init__(sheet, pos_x, pos_y, game, cols, rows, game.enemies_group)
        self.speedX = speedX
        self.speedY = speedY
        self.owner = owner
        self.rect = rect.copy()
        self.center = self.rect.center
        self.coord = Coord(pos_x, pos_y)

    def move(self):
        if self.check(self.coord.x + self.speedX, self.coord.y + self.speedY):
            self.coord += [self.speedX, self.speedY]
            self.rect.x += self.speedX * self.game.tile_width
            self.rect.y += self.speedY * self.game.tile_height
        else:
            self.owner.conflict(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.update_sprite(self.cur_frame + 0.3)
