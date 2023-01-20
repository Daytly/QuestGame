<<<<<<< HEAD
import time

import pygame
import mixer as mx
from text import Text
import os


class Button:
    def __init__(self, x, y, width, height,  massage, *args, staticColor=(0, 0, 0), activeColor=(0, 0, 0), size=30,
                 dis=10, action=None, image='none.png', rows=1, cols=1, imageIcon='none.png'):
        self.args = args
        self.width = width
        self.height = height
        self.staticColor = pygame.Color(staticColor[0], staticColor[1], staticColor[2])
        self.activeColor = pygame.Color(activeColor[0], activeColor[1], activeColor[2])
        self.dis = dis
        self.size = size
        self.action = action
        self.sheet = pygame.image.load(f'{os.getcwd()}/Data/sprites/buttons/{image}')
        self.frames = []
        self.cut_sheet(self.sheet, cols, rows)
        self.cur_frame = 0
        self.image = None
        self.update_sprite(0)
        self.useImage = image != 'none.png'
        self.rect = self.image.get_rect().move(x, y)
        self.icon = None
        self.rectIcon = None
        self.setIcon(imageIcon)
        self.text = self.createText(massage)
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
                        if not self.isPressed:
                            self.click()
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
            screen.blit(self.icon, [self.rectIcon.x, self.rectIcon.y + 2])
            self.text.buttonDownDraw(screen)
        else:
            screen.blit(self.icon, self.rectIcon)
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
        self.text.rect.y = self.rect.y + (self.height - 3 - self.text.height) // 2
        self.rectIcon = self.icon.get_rect().move(self.rect.x + (self.width - self.icon.get_width()) // 2,
                                                  self.rect.y + (self.height - 3 - self.icon.get_height()) // 2)

    def setText(self, massage):
        self.text = self.createText(massage)

    def createText(self, massage):
        text = Text(0, 0, (192, 203, 220), 30, massage)
        text.rect.x = self.rect.x + (self.width - text.width) // 2
        text.rect.y = self.rect.y + (self.height - 3 - text.height) // 2
        return text

    def getText(self):
        return self.text.message

    def setIcon(self, imageIcon):
        try:
            self.icon = pygame.image.load('Data/sprites/icons/' + imageIcon)
        except FileNotFoundError:
            print('Файл не найден')
        self.icon = pygame.transform.scale(self.icon, (self.icon.get_width() - 15, self.icon.get_height() - 15))
        self.rectIcon = self.icon.get_rect().move(self.rect.x + (self.width - self.icon.get_width()) // 2,
                                                  self.rect.y + (self.height - self.icon.get_height()) // 2 - 3)

    def click(self):
        if self.action:
            mx.mixer.play('button', loops=0)
            self.action(*self.args) if self.args else self.action()
            self.isPressed = True
=======
import time

import pygame
import mixer as mx
from text import Text


class Button:
    def __init__(self, x, y, width, height,  massage, *args, staticColor=(0, 0, 0), activeColor=(0, 0, 0), size=30,
                 dis=10, action=None, image='none.png', rows=1, cols=1, imageIcon='none.png'):
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
        self.icon = None
        self.rectIcon = None
        self.setIcon(imageIcon)
        self.text = self.createText(massage)
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
                        if not self.isPressed:
                            self.click()
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
            screen.blit(self.icon, [self.rectIcon.x, self.rectIcon.y + 2])
            self.text.buttonDownDraw(screen)
        else:
            screen.blit(self.icon, self.rectIcon)
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
        self.text.rect.y = self.rect.y + (self.height - 3 - self.text.height) // 2
        self.rectIcon = self.icon.get_rect().move(self.rect.x + (self.width - self.icon.get_width()) // 2,
                                                  self.rect.y + (self.height - 3 - self.icon.get_height()) // 2)

    def setText(self, massage):
        self.text = self.createText(massage)

    def createText(self, massage):
        text = Text(0, 0, (192, 203, 220), 30, massage)
        text.rect.x = self.rect.x + (self.width - text.width) // 2
        text.rect.y = self.rect.y + (self.height - 3 - text.height) // 2
        return text

    def getText(self):
        return self.text.message

    def setIcon(self, imageIcon):
        try:
            self.icon = pygame.image.load('Data/sprites/icons/' + imageIcon)
        except FileNotFoundError:
            print('Файл не найден')
        self.icon = pygame.transform.scale(self.icon, (self.icon.get_width() - 15, self.icon.get_height() - 15))
        self.rectIcon = self.icon.get_rect().move(self.rect.x + (self.width - self.icon.get_width()) // 2,
                                                  self.rect.y + (self.height - self.icon.get_height()) // 2 - 3)

    def click(self):
        if self.action:
            mx.mixer.play('button', loops=0)
            self.action(*self.args) if self.args else self.action()
            self.isPressed = True
>>>>>>> origin/master
