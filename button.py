import pygame
from functions import print_text


class Button:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def draw(self, screen, massage, staticColor, activeColor, dis=10, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x < mouse[0] < self.x + self.width:
            if self.y < mouse[1] < self.y + self.height:
                pygame.draw.rect(screen, staticColor, (self.x, self.y, self.width, self.height))
                if click[0] == 1:
                    # pygame.mixer.Sound.play(mp3_button)
                    # pygame.time.delay(170)
                    if action is not None:
                        action()
            else:
                pygame.draw.rect(screen, activeColor, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, activeColor, (self.x, self.y, self.width, self.height))
        print_text(screen, self.x + (self.width - len(massage) * 20) // 2, self.y + (self.height - 20) // 2,
                   30, massage, (200, 0, 0))


class ButtonLevel(Button):
    def __init__(self, width, height, x, y, level):
        super().__init__(width, height, x, y)
        self.level = level

    def get_level(self):
        return self.level

    def draw(self, screen, massage, staticColor, activeColor, dis=10, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x < mouse[0] < self.x + self.width:
            if self.y < mouse[1] < self.y + self.height:
                pygame.draw.rect(screen, staticColor, (self.x, self.y, self.width, self.height))
                if click[0] == 1:
                    if action is not None:
                        action(self.level)
            else:
                pygame.draw.rect(screen, activeColor, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, activeColor, (self.x, self.y, self.width, self.height))
        print_text(screen, self.x + (self.width - len(massage) * 10) // 2, self.y + 10, 20, massage, (200, 0, 0))