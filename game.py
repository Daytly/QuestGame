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
        self.tile_height = 48
        self.tile_width = 48
        self.screen = self.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.tile_images = {
            'wall': pygame.transform.scale(functions.load_image('barrier.png'), (96, 48)),
            'empty': pygame.transform.scale(functions.load_image('floor.png'), (144, 144)),
            'door': functions.load_image('door.png'),
            'player': pygame.transform.scale(functions.load_image('spriteSheet.png'), (192, 48)),
            'slime': pygame.transform.scale(functions.load_image('slime.png'), (192, 48)),
            'key': pygame.transform.scale(functions.load_image('key.png'), (96, 48)),
            'grass': pygame.transform.scale(functions.load_image('grass.png'), (96, 96)),
            'floorDetail': pygame.transform.scale(functions.load_image('floorDetail.png'), (768, 192)),
            'tree': pygame.transform.scale(functions.load_image('tree.png'), (48, 48)),
            'deadPlayer': pygame.transform.scale(functions.load_image('deadPlayer.png'), (48, 48))
        }
        self.enemies = []
        self.player = None
        self.camera = Camera(self)
        # группы спрайтов
        self.all_sprites = pygame.sprite.Group()
        self.tiles_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        level_list = functions.load_level('map.txt')
        self.level, self.player, self.enemies, self.level_x, self.level_y = functions.generate_levelInHouse(level_list, self)

    def run(self, name_level):
        self.enemies = []
        self.camera = Camera(self)
        self.all_sprites = pygame.sprite.Group()
        self.tiles_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        level_list = functions.load_level(name_level)
        enemyEventType = pygame.USEREVENT + 1
        pygame.time.set_timer(enemyEventType, 500)
        self.level, self.player, self.enemies, self.level_x, self.level_y = functions.generate_levelOutside(level_list, self)
        reset_btn = ButtonLevel(40, 40, 295, 650, name_level)
        menu_btn = Button(40, 40, 345, 650)
        while True:
            self.screen.fill(pygame.Color('white'))
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == enemyEventType:
                    for enemy in self.enemies:
                        enemy.move(event)
                self.player.update(event)
            # изменяем ракурс камеры
            self.camera.update(self.player)
            # обновляем положение всех спрайтов
            for sprite in self.all_sprites:
                self.camera.apply(sprite)
                sprite.draw(self.screen)
            reset_btn.draw(self.screen, 'R', (100, 100, 100), (150, 150, 150), action=self.run)
            menu_btn.draw(self.screen, 'M', (100, 100, 100), (150, 150, 150), action=self.menu)
            self.display.flip()
            if self.check_intersection():
                self.death()
                self.end_screen(False)

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
                    sys.exit()
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
                    sys.exit()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    return self.menu()
            pygame.display.flip()
            self.clock.tick(self.fps)

    def check_intersection(self):
        for i in self.enemies:
            if i.rect.center == self.player.rect.center:
                self.player.killer = i
                return True
        return False

    def death(self):
        death_img = self.tile_images['deadPlayer']
        for i in self.all_sprites:
            if i != self.player.killer and i != self.player:
                i.draw(self.screen)
        self.screen.blit(death_img, self.player.rect)
        self.display.flip()
        tick = 0
        while tick < 30:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            tick += 1
            self.clock.tick(self.fps)
        for i in self.all_sprites:
            if i != self.player.killer and i != self.player:
                i.draw(self.screen)
        self.screen.blit(death_img, self.player.rect)
        self.display.flip()
        tick = 0
        while tick < 60:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            tick += 1
            self.clock.tick(self.fps)


game = Game()
game.start_screen()
game.menu()
