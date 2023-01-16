import sys

import pygame
from coord import Coord
import os


class Picture:
    def __init__(self, x, y, path_file, width, height):
        if not os.path.isfile(path_file):
            print('Файл не найден')
            sys.exit()
        self.width = width
        self.height = height
        self.image = pygame.image.load(path_file)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect().move(x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def updateCoord(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def reSize(self, sizeX, sizeY):
        self.image = pygame.transform.scale(self.image, (sizeX, sizeY))
