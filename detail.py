import random

import pygame
from gameObject import GameObject


class Detail(GameObject):
    def __init__(self, sheet, pos_x, pos_y, game, cols, rows, numSprite):
        super().__init__(sheet, pos_x, pos_y, game, cols, rows)
        # for ind in range(len(self.frames)):
        # self.frames[ind] = pygame.transform.rotate(self.frames[ind], random.randrange(0, 361, 90))
        self.update_sprite(numSprite)
