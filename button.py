import pygame
from functions import print_text
import mixer as mx


class Button:
    def __init__(self, width, height, x, y, massage, staticColor, activeColor, *args, dis=10, action=None,
                 image='none.png',):
        self.args = args
        self.width = width
        self.height = height
        self.massage = massage
        self.staticColor = pygame.Color(staticColor[0], staticColor[1], staticColor[2])
        self.activeColor = pygame.Color(activeColor[0], activeColor[1], activeColor[2])
        self.dis = dis
        self.action = action
        self.image = pygame.transform.scale(pygame.image.load('Data/sprites/buttons/' + image), (width, height))
        self.useImage = image != 'none.png'
        self.rect = self.image.get_rect().move(x, y)
        self.isPressed = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.rect.x < mouse[0] < self.rect.x + self.width:
            if self.rect.y < mouse[1] < self.rect.y + self.height:
                if self.useImage:
                    pass
                else:
                    self.image.fill(self.staticColor)
                if click[0] == 1:
                    if self.action is not None and not self.isPressed:
                        mx.mixer.play('button', loops=1)
                        self.action(*self.args) if self.args else self.action()
                        self.isPressed = True
                else:
                    self.isPressed = False
            else:
                if self.useImage:
                    pass
                else:
                    self.image.fill(self.activeColor)
        else:
            if self.useImage:
                pass
            else:
                self.image.fill(pygame.Color(self.activeColor))
        print_text(screen, self.rect.x + (self.width - len(self.massage) * 20)//2, self.rect.y + (self.height - 20)//2,
                   30, self.massage, (200, 0, 0))

