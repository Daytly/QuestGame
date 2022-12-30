import pygame


class DynamicGameObject(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, game):
        super().__init__(game.player_group, game.all_sprites)
        self.image = game.tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            game.tile_width * pos_x + 15, game.tile_height * pos_y + 5)
        self.coord = [pos_x, pos_y]
        self.game = game

    def update(self, *args):
        pass

    def check(self, x, y):
        try:
            return self.game.level[y][x].stepOn()
        except IndexError:
            return False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
