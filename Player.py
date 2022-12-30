import pygame
from DynamicGameObject import DynamicGameObject


class Player(DynamicGameObject):
    def update(self, *args):
        if args and args[0].type == pygame.KEYDOWN:
            if args[0].key == pygame.K_UP:
                if self.check(self.coord[0], self.coord[1] - 1):
                    if self.rect.y >= self.game.tile_height:
                        self.rect.y -= 50
                        self.coord[1] -= 1
            if args[0].key == pygame.K_DOWN:
                if self.check(self.coord[0], self.coord[1] + 1):
                    self.rect.y += 50
                    self.coord[1] += 1
            if args[0].key == pygame.K_RIGHT:
                if self.check(self.coord[0] + 1, self.coord[1]):
                    self.rect.x += 50
                    self.coord[0] += 1
            if args[0].key == pygame.K_LEFT:
                if self.check(self.coord[0] - 1, self.coord[1]):
                    self.rect.x -= 50
                    self.coord[0] -= 1
