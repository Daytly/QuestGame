import sys

import pygame

from staticGameObject import StaticGameObject


class Portal(StaticGameObject):
    ol = None

    def __init__(self, sheet, pos_x, pos_y, game, cols, rows):
        super().__init__(sheet, pos_x, pos_y, game, cols, rows)
        self.other_ladder = None
        if not Portal.ol:
            Portal.ol = self
        else:
            self.other_ladder = Portal.ol
            Portal.ol.other_ladder = self
            Portal.ol = None

    def tap(self):
        if self.other_ladder:
            tick = 0
            surface = pygame.Surface((1000, 700))
            surface.fill(pygame.Color('black'))
            s_rect = pygame.Rect(-1000, 0, 700, 700)
            while tick <= 25:
                tick += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                self.game.all_sprites.draw(self.game.screen)
                self.game.screen.blit(surface, s_rect)
                s_rect.x += 40
                self.game.display.flip()
                self.game.clock.tick(60)

            self.game.player.rect.center = self.other_ladder.rect.center
            self.game.player.rect.y = self.game.player.rect.y + 48
            self.game.player.coord = self.other_ladder.coord.__copy__()
            self.game.player.coord += (0, 1)
            self.game.camera.move(self.game.player)
            for i in self.game.all_sprites:
                self.game.camera.apply(i)

            while tick <= 50:
                tick += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                self.game.all_sprites.draw(self.game.screen)
                self.game.screen.blit(surface, s_rect)
                s_rect.x += 40
                self.game.display.flip()
                self.game.clock.tick(60)

