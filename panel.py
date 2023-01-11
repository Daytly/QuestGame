import pygame
from button import Button


class Panel:
    def __init__(self, x, y, width, height, image, buttons):
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(pygame.image.load('Data/sprites/buttons/' + image),
                                            (self.width, self.height))
        self.rect = self.image.get_rect().move(x, y)
        self.buttons = buttons
        y = (self.height - sum([i.height for i in self.buttons]) - 160) // (len(self.buttons) - 1)
        sizeX = self.width - 160
        for indButton in range(len(self.buttons)):
            self.buttons[indButton].reSize(sizeX, self.buttons[indButton].height, 1, 3)
            self.buttons[indButton].rect.x = self.rect.x + 80
            if indButton > 0:
                self.buttons[indButton].rect.y = self.buttons[indButton - 1].height + y + \
                                                 self.buttons[indButton - 1].rect.y
            else:
                self.buttons[indButton].rect.y = self.rect.y + 80

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for button in self.buttons:
            button.draw(screen)

