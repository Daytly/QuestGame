import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, game):
        super().__init__(game.player_group, game.all_sprites)
        self.image = game.player_image
        self.rect = self.image.get_rect().move(
            game.tile_width * pos_x + 15, game.tile_height * pos_y + 5)
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
                if not self.isWall(self.coord[0], self.coord[1] + 1):
                    self.rect.y += 50
                    self.coord[1] += 1
            if args[0].key == pygame.K_RIGHT:
                if not self.isWall(self.coord[0] + 1, self.coord[1]):
                    self.rect.x += 50
                    self.coord[0] += 1
            if args[0].key == pygame.K_LEFT:
                if not self.isWall(self.coord[0] - 1, self.coord[1]):
                    self.rect.x -= 50
                    self.coord[0] -= 1

    def isWall(self, x, y):
        try:
            if self.game.level[y][x] != '#':
                return False
        except IndexError:
            return True
        return True

    def draw(self, screen):
        screen.blit(self.image, self.rect)
