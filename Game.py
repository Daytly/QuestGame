import sys
import pygame
from Camera import Camera
import Functions


class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display
        self.screen = self.display.set_mode((700, 700))
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.player = None
        self.level = Functions.load_level('map.txt')
        self.player, self.level_x, self.level_y = generate_level(level, self)
        self.camera = Camera()
        # группы спрайтов
        self.all_sprites = pygame.sprite.Group()
        self.tiles_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()

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
            self.camera.update(player)
            # обновляем положение всех спрайтов
            for sprite in self.all_sprites:
                self.camera.apply(sprite)
            self.display.flip()


game = Game()
game.run()
