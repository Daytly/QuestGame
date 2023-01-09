import pygame
from functions import print_text


class Button:
    def __init__(self, width, height, x, y, massage, staticColor, activeColor, dis=10, action=None, image='Data'
                                                                                                          '/sprites'
                                                                                                          '/none.png'):
        self.width = width
        self.height = height
        self.massage = massage
        self.staticColor = staticColor
        self.activeColor = activeColor
        self.dis = dis
        self.action = action
        self.image = pygame.transform.scale(pygame.image.load(image), (width, height))
        self.rect = self.image.get_rect().move(x, y)
        self.isPressed = True

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.rect.x < mouse[0] < self.rect.x + self.width:
            if self.rect.y < mouse[1] < self.rect.y + self.height:
                pygame.draw.rect(screen, self.staticColor, (self.rect.x, self.rect.y, self.width, self.height))
                if click[0] == 1:
                    # pygame.mixer.Sound.play(mp3_button)
                    # pygame.time.delay(170)
                    if self.action is not None and not self.isPressed:
                        self.action()
                        self.isPressed = True
                else:
                    self.isPressed = False
            else:
                pygame.draw.rect(screen, self.activeColor, (self.rect.x, self.rect.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.activeColor, (self.rect.x, self.rect.y, self.width, self.height))
        print_text(screen, self.rect.x + (self.width - len(self.massage) * 20)//2, self.rect.y + (self.height - 20)//2,
                   30, self.massage, (200, 0, 0))


class ButtonLevel(Button):
    def __init__(self, width, height, x, y, level, massage, staticColor, activeColor, action):
        super().__init__(width, height, x, y, massage, staticColor, activeColor, action=action)
        self.level = level

    def get_level(self):
        return self.level

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.rect.x < mouse[0] < self.rect.x + self.width:
            if self.rect.y < mouse[1] < self.rect.y + self.height:
                pygame.draw.rect(screen, self.staticColor, (self.rect.x, self.rect.y, self.width, self.height))
                if click[0] == 1: 
                    # pygame.mixer.Sound.play(mp3_button)
                    # pygame.time.delay(170)
                    if self.action is not None and not self.isPressed:
                        self.action(self.level)
                        self.isPressed = True
                else:
                    self.isPressed = False
            else:
                pygame.draw.rect(screen, self.activeColor, (self.rect.x, self.rect.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.activeColor, (self.rect.x, self.rect.y, self.width, self.height))
        print_text(screen, self.rect.x + (self.width - len(self.massage) * 20) // 2, self.rect.y + (self.height - 20) // 2,
                   30, self.massage, (200, 0, 0))
