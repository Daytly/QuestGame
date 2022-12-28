import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, game):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.coord = [pos_x, pos_y]
        self.game = game

    def update(self, *args):
        if args and args[0].type == pygame.KEYDOWN:
            if args[0].key == pygame.K_UP:
                if not self.isWall(self.coord[0], self.coord[1] - 1):
                    if self.rect.y >= self.game.tile_height:
                        self.rect.y -= 50
                        self.coord[1] -= 1
            if args[0].key == pygame.K_DOWN:
                if self.coord[1] >= 1:
                    if not self.isWall(self.coord[0], self.coord[1] + 1):
                        self.rect.y += 50
                        self.coord[1] += 1
            if args[0].key == pygame.K_RIGHT:
                if self.isWall(self.coord[0] + 1, self.coord[1]):
                    self.rect.x += 50
                    self.coord[0] += 1
            if args[0].key == pygame.K_LEFT:
                if self.isWall(self.coord[0] - 1, self.coord[1]):
                    self.rect.x -= 50
                    self.coord[0] -= 1

    def isWall(self, x, y):
        if len(self.game.level) > y >= 0 and len(self.game.level[0]) > x >= 0:
            if self.game.level[x][y] != '#':
                return False
        return True
