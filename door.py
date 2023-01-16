import pygame
from staticGameObject import StaticGameObject


class Door(StaticGameObject):
    def __init__(self, sheet, pos_x, pos_y, game, cols, rows, lock=False):
        super().__init__(sheet, pos_x, pos_y, game, cols, rows)
        self.solid = True
        self.lock = lock

    def unLock(self):
        self.lock = False

    def stepOn(self, entity):
        if not self.lock:
            self.game.end_screen(True)
            return self.solid
        return True
