import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, game):
        super().__init__(game.tiles_group, game.all_sprites)
        self.image = game.tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            game.tile_width * pos_x, game.tile_height * pos_y)