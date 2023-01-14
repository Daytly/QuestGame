import pygame


class OptionsMenu:
    def __init__(self, x, y, width, height, image, widgets):
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(pygame.image.load('Data/sprites/buttons/' + image),
                                            (self.width, self.height))
        self.rect = self.image.get_rect().move(x, y)
        self.widgets = widgets
        self.indActivePage = 0
        for indPage in range(len(self.widgets)):
            if len(self.widgets[indPage]) > 1:
                y = (self.height - sum([i.height for i in self.widgets[indPage]]) - 160)\
                    // (len(self.widgets[indPage]) - 1)
            else:
                y = 0
            sizeX = self.width - self.width // 3
            for ind in range(len(self.widgets[indPage])):
                self.widgets[indPage][ind].reSize(sizeX, self.widgets[indPage][ind].height, 1, 3)
                self.widgets[indPage][ind].rect.x = self.rect.x + (self.width - sizeX) // 2
                if ind > 0:
                    self.widgets[indPage][ind].rect.y = self.widgets[indPage][ind - 1].height + y + \
                                                     self.widgets[indPage][ind - 1].rect.y
                else:
                    self.widgets[indPage][ind].rect.y = self.rect.y + 80

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for widget in self.widgets[self.indActivePage]:
            widget.draw(screen)

    def nextPage(self):
        self.indActivePage += 1
        self.indActivePage %= len(self.widgets)

    def previousPage(self):
        self.indActivePage -= 1
        self.indActivePage %= len(self.widgets)
