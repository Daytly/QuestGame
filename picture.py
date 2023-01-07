import sys

import pygame
from coord import Coord
import os


class Picture:
    def __init__(self, x, y, path_file, sizeX, sizeY):
        if not os.path.isfile(path_file):
            print('Файл не найден')
            sys.exit()
        self.image = pygame.image.load(path_file)
        self.image = pygame.transform.scale(self.image, (sizeX, sizeY))
        self.rect = self.image.get_rect().move(x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
