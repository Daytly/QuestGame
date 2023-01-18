import pygame
from staticGameObject import StaticGameObject
import mixer as mx


class Door(StaticGameObject):
    def __init__(self, sheet, pos_x, pos_y, game, cols, rows, lock=False):
        super().__init__(sheet, pos_x, pos_y, game, cols, rows)
        self.solid = True
        self.lock = lock

    def unLock(self):
        self.lock = False

    def use(self):
        if self.lock:
            if self.game.player.has_key:
                self.unLock()
                mx.mixer.play('openDoor', loops=0)
                return
        else:
            self.game.end_screen(True)
