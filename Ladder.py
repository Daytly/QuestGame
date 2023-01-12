import sys

import pygame

from staticGameObject import StaticGameObject


class Ladder(StaticGameObject):
    ol = None

    def __init__(self, sheet, pos_x, pos_y, game, cols, rows):
        super().__init__(sheet, pos_x, pos_y, game, cols, rows)
        self.other_ladder = None
        if not Ladder.ol:
            Ladder.ol = self
        else:
            self.other_ladder = Ladder.ol
            Ladder.ol.other_ladder = self
            Ladder.ol = None

    def use(self):
        self.game.player.rect.center = self.other_ladder.rect.center
        self.game.player.coord = self.other_ladder.coord
        self.game.camera.move(self.game.player)
        for i in self.game.all_sprites:
            self.game.camera.apply(i)
