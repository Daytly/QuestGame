import sys

import pygame
from coord import Coord


class Picture:
    def __init__(self, x, y, path_file):
        if not os.path.isfile(fullname):
            print('Файл не найден')
            sys.exit()
        self.image = pygame.image.load(path_file)
        self.rect = self.image.get_rect().move(x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
