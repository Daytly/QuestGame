import pygame
import sys
from camera import Camera
from floor import Floor
from button import Button
from picture import Picture
from text import Text
from panel import Panel
import functions
from missile import Missile
from portal import Portal
from os import listdir, path
from optionsMenu import OptionsMenu
from rowWidgets import RowWidgets
import mixer as mx
from settings import Settings
import json
from CONSTANTS import keyAndValue


class Game:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
        for i in self.joysticks:
            i.init()
        self.joy_available = len(self.joysticks) > 0
        self.display = pygame.display
        self.display.set_caption('Samurai Storm')
        self.display.set_icon(pygame.image.load('Data/sprites/icon.png'))
        self.width = 700
        self.height = 700
        self.fps = 60
        self.tile_height = 48
        self.tile_width = 48
        self.screen = self.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        mx.mixer.play('menu', fade_ms=200)
        if not self.settings.isSound:
            mx.mixer.volume()
        self.tile_images = {
            'wall': pygame.transform.scale(functions.load_image('barrier.png'), (96, 48)),
            'empty': pygame.transform.scale(functions.load_image('floor.png'), (144, 144)),
            'door': pygame.transform.scale(functions.load_image('door.png'), (96, 48)),
            'player': pygame.transform.scale(functions.load_image('spriteSheet.png'), (188, 47)),
            'slime': pygame.transform.scale(functions.load_image('slime.png'), (192, 48)),
            'key': pygame.transform.scale(functions.load_image('key.png'), (96, 48)),
            'grass': pygame.transform.scale(functions.load_image('grass.png'), (96, 96)),
            'floorDetail': pygame.transform.scale(functions.load_image('floorDetail.png'), (768, 192)),
            'tree': pygame.transform.scale(functions.load_image('tree.png'), (48, 48)),
            'deadPlayer': pygame.transform.scale(functions.load_image('deadPlayer.png'), (48, 48)),
            'spikes': pygame.transform.scale(functions.load_image('spikes.png'), (480, 48)),
            'shuriken': pygame.transform.scale(functions.load_image('shuriken.png'), (96, 48)),
            'darkNinja': pygame.transform.scale((functions.load_image('darkNinja.png')), (192, 96)),
            "ladder": pygame.transform.scale(functions.load_image('portal.png'), (48, 48)),
            'startScreen': pygame.transform.scale(functions.load_image('startScreen.png'), (self.width, self.height)),
            'fon': pygame.transform.scale(functions.load_image('fon.png'), (self.width, self.height)),
            'sliderDot': functions.load_image('sliderDot.png'),
            'sliderLine': functions.load_image('sliderLine.png'),
            'coin': pygame.transform.scale(functions.load_image('coin.png'), (128, 32)),
            'key_test': pygame.transform.scale(functions.load_image('key(test).png'), (32, 32))
        }
        self.activeMenu = False
        self.activeOptionsMenu = False
        self.enemies = None
        self.coordSpikes = None
        self.player = None
        self.camera = None
        # ???????????? ????????????????
        self.all_sprites = None
        self.tiles_group = None
        self.player_group = None
        self.enemies_group = None
        self.ladders_group = None
        self.moneyCounter = None
        self.maxMoney = 0
        self.optionsMenu = self.createOptionMenu()
        self.updateBindButtonText()
        self.pageSwitches = [Button(5, 330, 40, 40, '', image='leftBtn.png', action=self.optionsMenu.previousPage,
                                    cols=3),
                             Button(655, 330, 40, 40, '', image='rightBtn.png', action=self.optionsMenu.nextPage,
                                    cols=3)]
        self.level, self.player, self.enemies, self.coordSpikes, self.level_x, self.level_y = \
            [None, None, None,
             None, None, None]
        self.dirLevels = listdir('Data/levels')
        self.indLevel = 0

    def run(self, name_level):
        self.enemies = []
        self.coordSpikes = []
        self.camera = Camera(self)
        self.all_sprites = pygame.sprite.Group()
        self.tiles_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.enemies_group = pygame.sprite.Group()
        self.activeMenu = False
        self.ladders_group = pygame.sprite.Group()
        level_list = functions.load_level(name_level)
        enemyEventType = pygame.USEREVENT + 1
        spikesEventType = enemyEventType + 1
        shurikenEventType = spikesEventType + 1
        pygame.time.set_timer(enemyEventType, 500)
        pygame.time.set_timer(spikesEventType, 300)
        pygame.time.set_timer(shurikenEventType, 100)  # ?????? ???????? ???? ???????????????????
        self.level, self.player, self.enemies, self.coordSpikes, self.maxMoney, self.level_x, self.level_y = \
            functions.generate_level(level_list, self, False)
        # ???????????????? ???????????? ????????????
        self.camera.move(self.player)
        # ?????????????????? ?????????????????? ???????? ????????????????
        for sprite in self.all_sprites:
            self.camera.apply(sprite)
            sprite.draw(self.screen)
        self.display.flip()

        pause_btn = Button(310, 620, 80, 80, '', action=self.openMenu,
                           image='pauseBtn.png')
        menu = Panel(100, 100, 500, 500,
                     'menuPanel1.png',
                     [Button(0, 0, 80, 80, 'PLAY', action=self.closeMenu,
                             image='buttonLong.png'),
                      Button(0, 0, 80, 80, 'OPTIONS', image='buttonLong.png', action=self.openOptionsMenu),
                      Button(0, 0, 80, 80, 'RESET', name_level, action=self.run, image='buttonLong.png'),
                      Button(0, 0, 80, 80, 'LEVELS', action=self.menu_levels,
                             image='buttonLong.png')])
        self.moneyCounter = RowWidgets(5, 0, 65, 50, [Picture(0, 0, 'Data/sprites/coinUI.png', 30, 30),
                                                      Text(0, 0, (0, 0, 0), 30, f'0')])
        self.moneyCounter[1].setText(f'0/{self.maxMoney}')
        pygame.image.save(self.screen, f'Data/screenShots/{name_level.rstrip(".txt")}SH.png')
        while True:
            self.screen.fill(pygame.Color('white'))
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == enemyEventType and not self.activeMenu:
                    for enemy in self.enemies:
                        if type(enemy) != Missile:
                            enemy.move()
                if event.type == shurikenEventType and not self.activeMenu:
                    for enemy in self.enemies:
                        if type(enemy) == Missile:
                            enemy.move()
                if event.type == spikesEventType and not self.activeMenu:
                    for y, x in self.coordSpikes:
                        self.level[y][x].update(event)
                if not self.activeMenu:
                    self.player.update(event)
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == self.settings.bindsJoystick['menu']:
                        if self.activeMenu:
                            self.closeMenu()
                        else:
                            self.openMenu()
                    if event.button == self.settings.bindsJoystick['exit'] and self.activeMenu:
                        self.menu()
                if event.type == pygame.KEYDOWN:
                    if event.key == self.settings.bindsKeyBoard['menu']:
                        if self.activeMenu:
                            self.closeMenu()
                        else:
                            self.openMenu()
            # ???????????????? ???????????? ????????????
            self.camera.update(self.player)
            # ?????????????????? ?????????????????? ???????? ????????????????
            for sprite in self.all_sprites:
                self.camera.apply(sprite)
                sprite.draw(self.screen)
            pause_btn.draw(self.screen)
            self.moneyCounter.draw(self.screen)
            if self.check_intersection():
                self.death()
                self.end_screen(False)
            if self.player.isDead():
                self.death()
                self.end_screen(False)
            if self.activeOptionsMenu:
                self.optionsMenu.draw(self.screen)
                for button in self.pageSwitches:
                    button.draw(self.screen)
            elif self.activeMenu:
                menu.draw(self.screen)
            self.display.flip()

    def start_screen(self):
        intro_text = []

        fon = self.tile_images['startScreen']
        self.screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 70)
        text_coordY = 500
        text_coordX = 100
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            text_coordY -= 10
            intro_rect.top = text_coordY
            intro_rect.x = text_coordX
            text_coordX += 40
            text_coordY += intro_rect.height
            self.screen.blit(string_rendered, intro_rect)
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    return  # ???????????????? ????????
                if event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYHATMOTION:
                    return
            pygame.display.flip()
            self.clock.tick(self.fps)

    def menu(self):
        print(self.settings.isSound)
        if self.settings.isSound:
            mx.mixer.setVolume('menu', 1)
        fon = self.tile_images['fon']
        self.screen.blit(fon, (0, 0))
        menu = Panel(100, 100, 500, 500,
                     'menuPanel1.png',
                     [Button(0, 0, 80, 80, 'PLAY', action=self.menu_levels,
                             image='buttonLong.png'),
                      Button(0, 0, 80, 80, 'OPTIONS', image='buttonLong.png', action=self.openOptionsMenu),
                      Button(0, 0, 80, 80, 'EXIT', image='buttonLong.png', action=sys.exit)])
        pygame.display.flip()
        while True:
            fon = self.tile_images['fon']
            self.screen.blit(fon, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == self.settings.bindsJoystick['menu']:
                        if self.activeOptionsMenu:
                            self.closeOptionsMenu()
                        else:
                            self.openOptionsMenu()
                    if event.button == self.settings.bindsJoystick['interact']:
                        self.menu_levels()
                    if event.button == self.settings.bindsJoystick['exit']:
                        sys.exit()
            if self.activeOptionsMenu:
                self.optionsMenu.draw(self.screen)
                for button in self.pageSwitches:
                    button.draw(self.screen)
            else:
                menu.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(self.fps)

    def menu_levels(self):
        fon = self.tile_images['fon']
        self.screen.blit(fon, (0, 0))
        levels = []
        for level in self.dirLevels:
            nameLevel = level.rstrip('.txt')
            levels.append([])
            levels[-1].append(Text(125, 20, (0, 0, 0), 50, nameLevel))
            if path.isfile(f'Data/screenShots/{nameLevel}SH.png'):
                levels[-1].append(Picture(125, 80, f'Data/screenShots/{nameLevel}SH.png', 450, 450))
            else:
                levels[-1].append(Picture(125, 80, f'Data/screenShots/none.png', 450, 450))
            levels[-1].append(Button(230, 570, 240, 80, 'Play', level,
                                     action=self.run, image='buttonLong.png', rows=3))

        menu_btn = Button(5, 635, 60, 60, '', action=self.menu, image='menuBtn.png',
                          cols=3, rows=1)
        right_btn = Button(635, 275, 60, 60, '', action=self.rightBtn,
                           image='rightBtn.png', cols=3, rows=1)
        left_btn = Button(5, 275, 60, 60, '', action=self.leftBtn,
                          image='leftBtn.png', cols=3, rows=1)
        while True:
            self.screen.fill((153, 217, 234))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == self.settings.bindsKeyBoard['right']:
                        self.rightBtn()
                    if event.key == self.settings.bindsKeyBoard['left']:
                        self.leftBtn()
                    if event.key == self.settings.bindsKeyBoard['interact']:
                        levels[self.indLevel][-1].click()
                if event.type == pygame.JOYHATMOTION:
                    x, y = self.joysticks[0].get_hat(0)
                    if x == 1:
                        self.rightBtn()
                    if x == -1:
                        self.leftBtn()
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:
                        self.run(self.dirLevels[self.indLevel])
                    if event.button == 7:
                        self.menu()
                    if event.button == self.settings.bindsJoystick['right']:
                        self.rightBtn()
                    if event.button == self.settings.bindsJoystick['left']:
                        self.leftBtn()
                    if event.button == self.settings.bindsJoystick['exit']:
                        self.menu()
            self.indLevel %= len(levels)
            for obj in levels[self.indLevel]:
                obj.draw(self.screen)
            menu_btn.draw(self.screen)
            left_btn.draw(self.screen)
            right_btn.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(self.fps)

    def end_screen(self, win):
        intro_text = "YOU'RE A WINNER" if win else "SKILL ISSUE"
        fon = self.tile_images['fon']
        color = (0, 180, 0) if win else (255, 60, 60)
        text = Text(0, 0, color, 60, intro_text)
        text.updateCoord((700 - text.width) // 2, (700 - text.height * 2) // 2)
        finalMoneyCounter = RowWidgets((700 - 80 - self.moneyCounter[1].width*3 - 5) // 2, 350, 170, 150,
                                       [Picture(0, 0, 'Data/sprites/coinUI.png', 80, 80),
                                        Text(0, 0, (0, 0, 0), 80, '0')])
        finalMoneyCounter[1].setText(self.moneyCounter[1].getText())
        while True:
            self.screen.blit(fon, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN or \
                        event.type == pygame.JOYBUTTONDOWN:
                    return self.menu()
            if win:
                finalMoneyCounter.draw(self.screen)
            text.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(self.fps)

    def check_intersection(self):
        entities = pygame.sprite.spritecollide(self.player, self.enemies_group, True)
        if entities:
            self.player.setKiller(entities[0])
            mx.mixer.setVolume('menu', 0)
            mx.mixer.play('hit', loops=0)
            return True
        return False

    def death(self):
        mx.mixer.play('gameOver', loops=0)
        death_img = self.tile_images['deadPlayer']
        for i in self.all_sprites:
            if i != self.player:
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
            if i != self.player:
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

    def rightBtn(self):
        self.indLevel = self.indLevel + 1

    def leftBtn(self):
        self.indLevel = self.indLevel - 1

    def openMenu(self):
        self.activeMenu = True

    def closeMenu(self):
        self.activeMenu = False

    def openOptionsMenu(self):
        self.activeOptionsMenu = True

    def closeOptionsMenu(self):
        self.settings.save(mx)
        self.activeOptionsMenu = False

    def createOptionMenu(self):
        return OptionsMenu(10, 10, 680, 680, image='menuPanel.png',
                           panels=[[Button(1, 1, 1, 60, 'ON/OFF sounds', image='buttonLong.png',
                                           action=mx.mixer.volume, size=20),
                                    Text(0, 0, (192, 203, 220), 50, 'KeyBoard Binds'),
                                    RowWidgets(0, 0, 0, 80,
                                               widgets=[Text(0, 0, (192, 203, 220), 30, 'UP'),
                                                        Button(1, 1, 200, 0, '0', 'up', False,
                                                               image='buttonLong.png',
                                                               action=self.binding, size=20)]),
                                    RowWidgets(0, 0, 0, 80,
                                               widgets=[Text(0, 0, (192, 203, 220), 30, 'DOWN'),
                                                        Button(1, 1, 200, 0, '0', 'down', False,
                                                               image='buttonLong.png',
                                                               action=self.binding, size=20)]),
                                    RowWidgets(0, 0, 0, 80,
                                               widgets=[Text(0, 0, (192, 203, 220), 30, 'RIGHT'),
                                                        Button(1, 1, 200, 0, '0', 'right', False,
                                                               image='buttonLong.png',
                                                               action=self.binding, size=15)]),
                                    RowWidgets(0, 0, 0, 80,
                                               widgets=[Text(0, 0, (192, 203, 220), 30, 'LEFT'),
                                                        Button(1, 1, 200, 0, '0', 'left', False,
                                                               image='buttonLong.png',
                                                               action=self.binding, size=15)]),
                                    Button(1, 1, 1, 60, 'Save and Back', image='buttonLong.png',
                                           action=self.closeOptionsMenu, size=20)],
                                   [RowWidgets(0, 0, 0, 80,
                                               widgets=[Text(0, 0, (192, 203, 220), 30, 'INTERACT'),
                                                        Button(1, 1, 200, 0, '0', 'interact', False,
                                                               image='buttonLong.png',
                                                               action=self.binding, size=15)]),
                                    RowWidgets(0, 0, 0, 80,
                                               widgets=[Text(0, 0, (192, 203, 220), 30, 'MENU'),
                                                        Button(1, 1, 200, 0, '0', 'menu', False,
                                                               image='buttonLong.png',
                                                               action=self.binding, size=15)]),
                                    Text(0, 0, (192, 203, 220), 50, 'Joystick Binds'),
                                    RowWidgets(0, 0, 0, 80,
                                               widgets=[Text(0, 0, (192, 203, 220), 30, 'UP'),
                                                        Button(1, 1, 200, 0, '0', 'up', True,
                                                               image='buttonLong.png',
                                                               action=self.binding, size=15)]),
                                    RowWidgets(0, 0, 0, 80,
                                               widgets=[Text(0, 0, (192, 203, 220), 30, 'DOWN'),
                                                        Button(1, 1, 200, 0, '0', 'down', True,
                                                               image='buttonLong.png',
                                                               action=self.binding, size=15)]),
                                    RowWidgets(0, 0, 0, 80,
                                               widgets=[Text(0, 0, (192, 203, 220), 30, 'RIGHT'),
                                                        Button(1, 1, 200, 0, '0', 'right', True,
                                                               image='buttonLong.png',
                                                               action=self.binding, size=15)]),
                                    Button(1, 1, 1, 60, 'Save and Back', image='buttonLong.png',
                                           action=self.closeOptionsMenu, size=20)],
                                   [RowWidgets(0, 0, 0, 80,
                                               widgets=[Text(0, 0, (192, 203, 220), 30, 'LEFT'),
                                                        Button(1, 1, 200, 0, '0', 'left', True,
                                                               image='buttonLong.png',
                                                               action=self.binding, size=15)]),
                                    RowWidgets(0, 0, 0, 80,
                                               widgets=[Text(0, 0, (192, 203, 220), 30, 'INTERACT'),
                                                        Button(1, 1, 200, 0, '0', 'interact', True,
                                                               image='buttonLong.png',
                                                               action=self.binding, size=15)]),
                                    RowWidgets(0, 0, 0, 80,
                                               widgets=[Text(0, 0, (192, 203, 220), 30, 'MENU'),
                                                        Button(1, 1, 200, 0, '0', 'menu', True,
                                                               image='buttonLong.png',
                                                               action=self.binding, size=15)]),
                                    RowWidgets(0, 0, 0, 80,
                                               widgets=[Text(0, 0, (192, 203, 220), 30, 'EXIT'),
                                                        Button(1, 1, 200, 0, '0', 'exit', True,
                                                               image='buttonLong.png',
                                                               action=self.binding, size=15)]),
                                    Button(1, 1, 1, 60, 'Save and Back', image='buttonLong.png',
                                           action=self.closeOptionsMenu, size=20)]])

    def binding(self, key, useJoystick):
        isSearch = True
        if useJoystick:
            while isSearch:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.JOYBUTTONDOWN:
                        self.settings.bindsJoystick[key] = event.button
                        isSearch = False
                        break
        else:
            while isSearch:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        self.settings.bindsKeyBoard[key] = event.key
                        isSearch = False
                        break
        self.updateBindButtonText()

    def updateBindButtonText(self):
        useJoystick = False
        useKeyBoard = False
        for indPage in range(len(self.optionsMenu)):
            for indWidget in range(len(self.optionsMenu[indPage])):
                if type(self.optionsMenu[indPage][indWidget]) == RowWidgets:
                    key = self.optionsMenu[indPage][indWidget][0].getText().lower()
                    icon = 'none.png'
                    if useJoystick:
                        try:
                            _str = keyAndValue[self.settings.bindsJoystick[key]]
                        except KeyError:
                            _str = 'None'
                        if '.png' in _str:
                            icon = _str
                            _str = ''
                        self.optionsMenu[indPage][indWidget][1].setIcon(icon)
                        self.optionsMenu[indPage][indWidget][1].setText(_str)
                    elif useKeyBoard:
                        try:
                            _str = keyAndValue[self.settings.bindsKeyBoard[key]]
                        except KeyError:
                            _str = 'None'
                        self.optionsMenu[indPage][indWidget][1].setIcon(icon)
                        self.optionsMenu[indPage][indWidget][1].setText(keyAndValue[self.settings.bindsKeyBoard[key]])
                elif type(self.optionsMenu[indPage][indWidget]) == Text:
                    if self.optionsMenu[indPage][indWidget].getText() == 'Joystick Binds':
                        useJoystick = True
                        useKeyBoard = False
                    elif self.optionsMenu[indPage][indWidget].getText() == 'KeyBoard Binds':
                        useKeyBoard = True
                        useJoystick = False

    def updateMoneyCounter(self, count):
        self.moneyCounter[1].setText(f'{count}/{self.maxMoney}')


game = Game()
game.start_screen()
game.menu()
