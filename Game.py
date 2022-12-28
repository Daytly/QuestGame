import sys
import pygame
from Camera import Camera
from Tile import Tile
import Functions


class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display
        self.width = 700
        self.height = 700
        self.screen = self.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.tile_height = 50
        self.tile_width = 50
        self.player_image = Functions.load_image('mar.png')
        self.tile_images = {
            'wall': Functions.load_image('box.png'),
            'empty': Functions.load_image('grass.png')
        }
        self.player = None
        self.camera = Camera(self)
        # группы спрайтов
        self.all_sprites = pygame.sprite.Group()
        self.tiles_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.level = Functions.load_level('map.txt')
        self.player, self.level_x, self.level_y = Functions.generate_level(self.level, self)

    def run(self):
        while True:
            self.screen.fill(pygame.Color('white'))
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.all_sprites.update(event)
            # изменяем ракурс камеры
            self.camera.update(self.player)
            # обновляем положение всех спрайтов
            for sprite in self.all_sprites:
                self.camera.apply(sprite)
            self.display.flip()


game = Game()
game.run()
