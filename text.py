import pygame
from coord import Coord


class Text:
    def __init__(self, x, y, color, size, text):
        font = pygame.font.Font('Data/fonts/pixelFont.ttf', size)
        self.text = font.render(text, 0, color)
        self.width, self.height = font.size(text)
        self.message = text
        self.color = color
        self.rect = Coord(x, y)

    def updateCoord(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.text, self.rect.get())

    def buttonDownDraw(self, screen):
        coord = self.rect + Coord(0, 2)
        screen.blit(self.text, coord.get())
