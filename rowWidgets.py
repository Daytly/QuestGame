import pygame
from coord import Coord
from text import Text


class LineWidgets:
    def __init__(self, x, y, width, height, widgets):
        self.width = width
        self.height = height
        self.rect = Coord(x, y)
        self.widgets = widgets
        self.changeCoordAndSize(3, 1)

    def draw(self, screen):
        for widget in self.widgets:
            widget.draw(screen)

    def reSize(self, sizeX, sizeY, col, row):
        self.width = sizeX
        self.height = sizeY
        self.changeCoordAndSize(col, row)

    def updateCoord(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.changeCoordAndSize(3, 1)

    def changeCoordAndSize(self, col, row):
        sizeY = self.height - self.height // 3
        indent = (self.width - sum([i.width for i in self.widgets])) // (len(self.widgets) + 1)
        x = indent + self.rect.x
        y = self.rect.y + (self.height - self.widgets[0].height) // 2
        self.widgets[0].updateCoord(x, y)
        for ind in range(1, len(self.widgets)):
            if type(self.widgets[ind]) != Text:
                self.widgets[ind].reSize(self.widgets[ind].width, sizeY, row, col)
            x = self.widgets[ind - 1].width + indent + self.widgets[ind - 1].rect.x
            y = self.rect.y + (self.height - self.widgets[ind].height) // 2
            self.widgets[ind].updateCoord(x, y)
