import pygame
from dynamicGameObject import DynamicGameObject
from key import Key
from door import Door


class Player(DynamicGameObject):
    def __init__(self, tile_type, pos_x, pos_y, game):
        super().__init__(tile_type, pos_x, pos_y, game)
        self.rect = self.image.get_rect().move(game.tile_width * pos_x + 15, game.tile_height * pos_y + 5)
        self.key = False

    def update(self, *args):
        if args and args[0].type == pygame.KEYDOWN:
            if args[0].key == pygame.K_UP:
                if self.check(self.coord.x, self.coord.y - 1):
                    if self.rect.y >= self.game.tile_height:
                        self.rect.y -= 50
                        self.coord.y -= 1
            if args[0].key == pygame.K_DOWN:
                if self.check(self.coord.x, self.coord.y + 1):
                    self.rect.y += 50
                    self.coord.y += 1
            if args[0].key == pygame.K_RIGHT:
                if self.check(self.coord.x + 1, self.coord.y):
                    self.rect.x += 50
                    self.coord.x += 1
            if args[0].key == pygame.K_LEFT:
                if self.check(self.coord.x - 1, self.coord.y):
                    self.rect.x -= 50
                    self.coord.x -= 1

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
