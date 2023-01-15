import pygame
from button import Button
from text import Text


class Panel:
    def __init__(self, x, y, width, height, image, widgets, froTheBeginning=False):
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(pygame.image.load('Data/sprites/buttons/' + image),
                                            (self.width, self.height))
        self.rect = self.image.get_rect().move(x, y)
        self.widgets = widgets
        if len(self.widgets) > 1:
            if froTheBeginning:
                indent = 3
            else:
                indent = (self.height - sum([i.height for i in self.widgets]) - 160) // (len(self.widgets) - 1)
        else:
            indent = 0
        sizeX = self.width - self.width // 3
        for ind in range(len(self.widgets)):
            if type(self.widgets[ind]) != Text:
                self.widgets[ind].reSize(sizeX, self.widgets[ind].height, 1, 3)
            x = self.rect.x + (self.width - sizeX) // 2
            if len(self.widgets) - 1 > ind > 0:
                y = self.widgets[ind - 1].height + indent + self.widgets[ind - 1].rect.y
            elif ind == 0:
                y = self.rect.y + 80
            else:
                y = self.rect.y + self.height - 80 - self.widgets[ind].height
            self.widgets[ind].updateCoord(x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for button in self.widgets:
            button.draw(screen)

    def __getitem__(self, item):
        if item >= len(self.widgets):
            raise IndexError
        else:
            return self.widgets[item]
