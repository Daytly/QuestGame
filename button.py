import time

import pygame
import mixer as mx
from text import Text


class Button:
    def __init__(self, x, y, width, height,  massage, *args, staticColor=(0, 0, 0), activeColor=(0, 0, 0), size=30,
                 dis=10, action=None, image='none.png', rows=1, cols=1):
        self.args = args
        self.width = width
        self.height = height
        self.staticColor = pygame.Color(staticColor[0], staticColor[1], staticColor[2])
        self.activeColor = pygame.Color(activeColor[0], activeColor[1], activeColor[2])
        self.dis = dis
        self.size = size
        self.action = action
        self.sheet = pygame.image.load('Data/sprites/buttons/' + image)
        self.frames = []
        self.cut_sheet(self.sheet, cols, rows)
        self.cur_frame = 0
        self.image = None
        self.update_sprite(0)
        self.useImage = image != 'none.png'
        self.rect = self.image.get_rect().move(x, y)
        self.text = Text(0, 0, (192, 203, 220), 30, massage)
        self.text.rect.x = self.rect.x + (self.width - self.text.width) // 2
        self.text.rect.y = self.rect.y + (self.height - self.text.height) // 2
        self.isPressed = True
        self.isClick = False

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        screen.blit(self.image, self.rect)
        if self.rect.x < mouse[0] < self.rect.x + self.width:
            if self.rect.y < mouse[1] < self.rect.y + self.height:
                if self.useImage:
                    self.update_sprite(2)
                else:
                    self.image.fill(self.activeColor)
                if click[0] == 1:
                    self.update_sprite(1)
                    screen.blit(self.image, self.rect)
                    self.isClick = True
                else:
                    if self.isClick:
                        if self.action is not None and not self.isPressed:
                            mx.mixer.play('button', loops=0)
                            self.action(*self.args) if self.args else self.action()
                            self.isPressed = True
                    self.isClick = False
                    self.isPressed = False
            else:
                self.isClick = False
                if self.useImage:
                    self.update_sprite(0)
                else:
                    self.image.fill(self.staticColor)
        else:
            self.isClick = False
            if self.useImage:
                self.update_sprite(0)
            else:
                self.image.fill(pygame.Color(self.staticColor))
        if self.isClick:
            self.text.buttonDownDraw(screen)
        else:
            self.text.draw(screen)

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

    def reSize(self, sizeX, sizeY, cols, rows):
        self.width = sizeX
        self.height = sizeY
        self.frames = []
        self.cut_sheet(self.sheet, cols, rows)
        self.update_sprite(0)

    def updateCoord(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.text.rect.x = self.rect.x + (self.width - self.text.width) // 2
        self.text.rect.y = self.rect.y + (self.height - self.text.height) // 2



