import sys

import pygame
from Ufo import Ufo


class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display
        self.screen = self.display.set_mode((700, 700))
        self.clock = pygame.time.Clock()
        self.fps = 60

    def run(self):
        while True:
            self.screen.fill(pygame.Color('white'))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.display.flip()
            self.clock.tick(self.fps)


game = Game()
game.run()
