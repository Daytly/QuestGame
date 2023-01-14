import pygame
from dynamicGameObject import DynamicGameObject
from key import Key
from door import Door
from spikes import Spikes
from binds import bindsKeyBoard, bindsJoystick


class Player(DynamicGameObject):
    def __init__(self, sheet, pos_x, pos_y, game):
        super().__init__(sheet, pos_x, pos_y, game, 4, 1, game.player_group)
        self.rect = self.image.get_rect().move(game.tile_width * pos_x + 1, game.tile_height * pos_y + 1)
        self.key = False
        self.killer = None  # Тот кто убил персонажа

    def update(self, *args):
        if args and args[0].type == pygame.JOYHATMOTION:
            x, y = self.game.joysticks[0].get_hat(0)
            if y == 1:
                if self.check(self.coord.x, self.coord.y - 1):
                    self.rect.y -= self.game.tile_height
                    self.coord.y -= 1
                self.update_sprite(1)
            if y == -1:
                if self.check(self.coord.x, self.coord.y + 1):
                    self.rect.y += self.game.tile_height
                    self.coord.y += 1
                self.update_sprite(0)
            if x == 1:
                if self.check(self.coord.x + 1, self.coord.y):
                    self.rect.x += self.game.tile_width
                    self.coord.x += 1
                self.update_sprite(3)
            if x == -1:
                if self.check(self.coord.x - 1, self.coord.y):
                    self.rect.x -= self.game.tile_width
                    self.coord.x -= 1
                self.update_sprite(2)
            self.image = self.frames[self.cur_frame]
        if args[0].type == pygame.JOYBUTTONDOWN:
            if args[0].button in bindsJoystick['interact']:
                for ladder in self.game.ladders_group:
                    if ladder.coord == self.coord:
                        ladder.use()
                        break
        if args and args[0].type == pygame.KEYDOWN:
            if args[0].key in bindsKeyBoard['up']:
                if self.check(self.coord.x, self.coord.y - 1):
                    self.rect.y -= self.game.tile_height
                    self.coord.y -= 1
                self.update_sprite(1)
            if args[0].key in bindsKeyBoard['down']:
                if self.check(self.coord.x, self.coord.y + 1):
                    self.rect.y += self.game.tile_height
                    self.coord.y += 1
                self.update_sprite(0)
            if args[0].key in bindsKeyBoard['left']:
                if self.check(self.coord.x - 1, self.coord.y):
                    self.rect.x -= self.game.tile_width
                    self.coord.x -= 1
                self.update_sprite(2)
            if args[0].key in bindsKeyBoard['right']:
                if self.check(self.coord.x + 1, self.coord.y):
                    self.rect.x += self.game.tile_width
                    self.coord.x += 1
                self.update_sprite(3)
            self.image = self.frames[self.cur_frame]
            if args[0].key in bindsKeyBoard['interact']:
                for ladder in self.game.ladders_group:
                    if ladder.coord == self.coord:
                        ladder.use()
                        break
        self.check(self.coord.x, self.coord.y)

    def check(self, x, y):
        try:
            _type = type(self.game.level[y][x])
            if _type == Key and not self.key:
                self.key = True
            elif _type == Door and self.key:
                self.game.level[y][x].unLock()
                self.key = False
            elif _type == Spikes:
                if self.game.level[y][x].isActive():
                    self.killer = self.game.level[y][x]
            return self.game.level[y][x].stepOn(self)
        except IndexError:
            return False

    def isDead(self):
        return self.killer

    def murder(self, killer):
        self.killer = killer

    def get_coord(self):
        return self.coord

    def setKiller(self, killer):
        self.killer = killer
