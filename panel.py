import pygame
from button import Button


class Panel:
    def __init__(self, x, y, width, height, image, widgets):
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(pygame.image.load('Data/sprites/buttons/' + image),
                                            (self.width, self.height))
        self.rect = self.image.get_rect().move(x, y)
        self.widgets = widgets
        if len(self.widgets) > 1:
            y = (self.height - sum([i.height for i in self.widgets]) - 160) // (len(self.widgets) - 1)
        else:
            y = 0
        sizeX = self.width - self.width // 3
        for ind in range(len(self.widgets)):
            self.widgets[ind].reSize(sizeX, self.widgets[ind].height, 1, 3)
            self.widgets[ind].rect.x = self.rect.x + (self.width - sizeX) // 2
            if ind > 0:
                self.widgets[ind].rect.y = self.widgets[ind - 1].height + y + \
                                                 self.widgets[ind - 1].rect.y
            else:
                self.widgets[ind].rect.y = self.rect.y + 80

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for button in self.widgets:
            button.draw(screen)

