import pygame
from panel import Panel


class OptionsMenu:
    def __init__(self, x, y, width, height, image, panels):
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(pygame.image.load('Data/sprites/buttons/' + image),
                                            (self.width, self.height))
        self.rect = self.image.get_rect().move(x, y)
        self.pages = []
        self.indActivePage = 0
        for indPage in range(len(panels)):
            self.pages.append(Panel(x, y, width, height, image, panels[indPage], froTheBeginning=True))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.pages[self.indActivePage].draw(screen)

    def nextPage(self):
        self.indActivePage += 1
        self.indActivePage %= len(self.pages)

    def previousPage(self):
        self.indActivePage -= 1
        self.indActivePage %= len(self.pages)

