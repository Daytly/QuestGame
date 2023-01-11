import pygame
from coord import Coord


class Text:
    def __init__(self, x, y, color, size, text):
        font = pygame.font.Font('Data/fonts/pixelFont.ttf', size)
        self.text = font.render(text, True, color)
        self.coord = Coord(x, y)

    def draw(self, screen):
        screen.blit(self.text, self.coord.get())

