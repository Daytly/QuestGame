import sys
import time
import pygame
from camera import Camera
from floor import Floor
from button import Button, ButtonLevel
import functions
from os import listdir


class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display
        self.width = 700
        self.height = 700
        self.fps = 60
        self.tile_height = 50
        self.tile_width = 50
        self.screen = self.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.tile_images = {
            'wall': functions.load_image('box.png'),
            'empty': functions.load_image('grass.png'),
            'door': functions.load_image('door.png'),
            'player': functions.load_image('mar.png'),
            'key': functions.load_image('key.png'),
        }
        self.player = None
        self.camera = Camera(self)
        # группы спрайтов
        self.all_sprites = pygame.sprite.Group()
        self.tiles_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        level_list = functions.load_level('map.txt')
        self.level, self.player, self.level_x, self.level_y = functions.generate_level(level_list, self)

    def run(self, name_level):
        self.camera = Camera(self)
        self.all_sprites = pygame.sprite.Group()
        self.tiles_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        level_list = functions.load_level(name_level)
        self.level, self.player, self.level_x, self.level_y = functions.generate_level(level_list, self)
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

        fon = pygame.transform.scale(functions.load_image('fon.png'), (self.width, self.height))
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
        pygame.display.flip()
        time.sleep(0.5)
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
        fon = pygame.transform.scale(functions.load_image('fon.png'), (self.width, self.height))
        self.screen.blit(fon, (0, 0))
        play_btn = Button(400, 70, 150, 250)
        exit_btn = Button(200, 40, 250, 350)
        play_btn.draw(self.screen, 'PLAY', (100, 100, 100), (150, 150, 150))
        exit_btn.draw(self.screen, 'EXIT', (100, 100, 100), (150, 150, 150))
        pygame.display.flip()
        time.sleep(0.5)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            play_btn.draw(self.screen, 'PLAY', (100, 100, 100), (150, 150, 150), action=self.menu_levels)
            exit_btn.draw(self.screen, 'EXIT', (100, 100, 100), (150, 150, 150), action=sys.exit)
            pygame.display.flip()
            self.clock.tick(self.fps)

    def menu_levels(self):
        fon = pygame.transform.scale(functions.load_image('fon.png'), (self.width, self.height))
        self.screen.blit(fon, (0, 0))
        # play_btn = Button(200, 40, 0, 0)
        # exit_btn = Button(200, 40, 0, 0)
        buttons = []
        dirLevels = listdir('Data/levels')
        for i in range(9):
            for j in range(9):
                if dirLevels:
                    buttons.append(ButtonLevel(60, 60, j * 70 + 40, i * 70 + 6, dirLevels.pop(0)))
        menu_btn = Button(60, 60, 5, 635)
        for level in buttons:
            level.draw(self.screen, level.get_level().rstrip('.txt'), (100, 100, 100), (150, 150, 150))
        menu_btn.draw(self.screen, 'M', (100, 100, 100), (150, 150, 150))
        pygame.display.flip()
        time.sleep(0.5)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            for level in buttons:
                level.draw(self.screen, level.get_level().rstrip('.txt'), (100, 100, 100), (150, 150, 150),
                           action=self.run)
            menu_btn.draw(self.screen, 'M', (100, 100, 100), (150, 150, 150), action=self.menu)
            pygame.display.flip()
            self.clock.tick(self.fps)

    def end_screen(self, win):
        intro_text = ["Ты победил" if win else "Ты проиграл"]

        fon = pygame.transform.scale(functions.load_image('fon.png'), (self.width, self.height))
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
        pygame.display.flip()
        time.sleep(0.5)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    return self.menu()
            pygame.display.flip()
            self.clock.tick(self.fps)


game = Game()
game.start_screen()
game.menu()