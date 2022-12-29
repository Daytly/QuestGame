import sys
import time

import pygame
from Camera import Camera
from Floor import Floor
from Button import Button, ButtonLevel
import Functions
from os import listdir


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
        level_list = Functions.load_level('map.txt')
        self.level, self.player, self.level_x, self.level_y = Functions.generate_level(level_list, self)

    def run(self, name_level):
        self.camera = Camera(self)
        self.all_sprites = pygame.sprite.Group()
        self.tiles_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        level_list = Functions.load_level(name_level)
        self.level, self.player, self.level_x, self.level_y = Functions.generate_level(level_list, self)
        reset_btn = ButtonLevel(40, 40, 295, 650, name_level)
        menu_btn = Button(40, 40, 345, 650)
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
                sprite.draw(self.screen)
            reset_btn.draw(self.screen, 'R', (100, 100, 100), (150, 150, 150), action=self.run)
            menu_btn.draw(self.screen, 'M', (100, 100, 100), (150, 150, 150), action=self.menu)
            self.display.flip()

    def start_screen(self):
        intro_text = ["ЗАСТАВКА", "",
                      "Правила игры",
                      "Если в правилах несколько строк,",
                      "приходится выводить их построчно"]

        fon = pygame.transform.scale(Functions.load_image('fon.png'), (self.width, self.height))
        self.screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            self.screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    time.sleep(0.5)
                    return  # начинаем игру
            pygame.display.flip()
            self.clock.tick(self.fps)

    def menu(self):
        fon = pygame.transform.scale(Functions.load_image('fon.png'), (self.width, self.height))
        self.screen.blit(fon, (0, 0))
        play_btn = Button(400, 70, 150, 250)
        exit_btn = Button(200, 40, 250, 350)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            play_btn.draw(self.screen, 'PLAY', (100, 100, 100), (150, 150, 150), action=self.menu_levels)
            exit_btn.draw(self.screen, 'EXIT', (100, 100, 100), (150, 150, 150), action=sys.exit)
            pygame.display.flip()
            self.clock.tick(self.fps)

    def menu_levels(self):
        time.sleep(0.5)
        fon = pygame.transform.scale(Functions.load_image('fon.png'), (self.width, self.height))
        self.screen.blit(fon, (0, 0))
        # play_btn = Button(200, 40, 0, 0)
        # exit_btn = Button(200, 40, 0, 0)
        buttons = []
        dirLevels = listdir('Data/levels')
        for i in range(10):
            for j in range(10):
                if dirLevels:
                    buttons.append(ButtonLevel(50, 50, j * 60 + 10, i * 60 + 10, dirLevels.pop(0)))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            for level in buttons:
                level.draw(self.screen, level.get_level().rstrip('.txt'), (100, 100, 100), (150, 150, 150),
                           action=self.run)
            # exit_btn.draw(self.screen, 'EXIT', (100, 100, 100), (150, 150, 150), action=sys.exit())
            pygame.display.flip()
            self.clock.tick(self.fps)


game = Game()
game.start_screen()
game.menu()
