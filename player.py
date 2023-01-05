import pygame
from dynamicGameObject import DynamicGameObject
from key import Key
from door import Door


class Player(DynamicGameObject):
    def __init__(self, sheet, pos_x, pos_y, game):
        super().__init__(sheet, pos_x, pos_y, game, 4, 1)
        self.rect = self.image.get_rect().move(game.tile_width * pos_x + 1, game.tile_height * pos_y + 1)
        self.key = False

    def update(self, *args):
        if args and args[0].type == pygame.KEYDOWN:
            if args[0].key == pygame.K_UP:
                if self.check(self.coord.x, self.coord.y - 1):
                    self.rect.y -= 50
                    self.coord.y -= 1
                self.cur_frame = 1
            if args[0].key == pygame.K_DOWN:
                if self.check(self.coord.x, self.coord.y + 1):
                    self.rect.y += 50
                    self.coord.y += 1
                self.cur_frame = 0
            if args[0].key == pygame.K_RIGHT:
                if self.check(self.coord.x + 1, self.coord.y):
                    self.rect.x += 50
                    self.coord.x += 1
                self.cur_frame = 3
            if args[0].key == pygame.K_LEFT:
                if self.check(self.coord.x - 1, self.coord.y):
                    self.rect.x -= 50
                    self.coord.x -= 1
                self.cur_frame = 2
            self.image = self.frames[self.cur_frame]

    def check(self, x, y):
        try:
            _type = type(self.game.level[y][x])
            if _type == Key and not self.key:
                self.key = True
            elif _type == Door and self.key:
                self.game.level[y][x].unLock()
                self.key = False
            return self.game.level[y][x].stepOn()
        except IndexError:
            return False
