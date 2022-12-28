import pygame


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, x, y, massage, color1, color2, color3, color4=20, color5=20, color6=200, dis=10, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(display, (color1, color2, color3), (x, y, self.width, self.height))
                if click[0] == 1:
                    # pygame.mixer.Sound.play(mp3_button)
                    # pygame.time.delay(170)
                    if action is not None:
                        action()
            else:
                pygame.draw.rect(display, (color4, color5, color6), (x, y, self.width, self.height))
        else:
            pygame.draw.rect(display, (color4, color5, color6), (x, y, self.width, self.height))
        print_text(x+dis, y+7, 30, massage, '', 200, 0, 0)
