import pygame
from functions import print_text
import mixer as mx


class Button:
    def __init__(self, width, height, x, y, massage, staticColor, activeColor, *args, dis=10, action=None,
                 image='none.png', rows=1, cols=1):
        self.args = args
        self.width = width
        self.height = height
        self.massage = massage
        self.staticColor = pygame.Color(staticColor[0], staticColor[1], staticColor[2])
        self.activeColor = pygame.Color(activeColor[0], activeColor[1], activeColor[2])
        self.dis = dis
        self.action = action
        self.sheet = pygame.image.load('Data/sprites/buttons/' + image)
        self.frames = []
        self.cut_sheet(self.sheet, cols, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.useImage = image != 'none.png'
        self.rect = self.image.get_rect().move(x, y)
        self.isPressed = True

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        screen.blit(self.image, self.rect)
        if self.rect.x < mouse[0] < self.rect.x + self.width:
            if self.rect.y < mouse[1] < self.rect.y + self.height:
                if self.useImage:
                    pass
                else:
                    self.image.fill(self.activeColor)
                if click[0] == 1:
                    if self.action is not None and not self.isPressed:
                        mx.mixer.play('button', loops=0)
                        self.action(*self.args) if self.args else self.action()
                        self.isPressed = True
                else:
                    self.isPressed = False
            else:
                if self.useImage:
                    pass
                else:
                    self.image.fill(self.staticColor)
        else:
            if self.useImage:
                pass
            else:
                self.image.fill(pygame.Color(self.staticColor))
        print_text(screen, self.rect.x + (self.width - len(self.massage) * 20)//2, self.rect.y + (self.height - 20)//2,
                   30, self.massage, (200, 0, 0))

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(pygame.transform.scale(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)), (self.width, self.height)))

    def update_sprite(self, numSprite):
        self.cur_frame = numSprite % len(self.frames)
        self.image = self.frames[int(self.cur_frame % len(self.frames))]


