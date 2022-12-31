import os
import pygame
from player import Player
from wall import Wall
from floor import Floor
from door import Door
from key import Key
import sys


def load_image(name, colorKey=None):
    fullname = os.path.join('Data/sprites', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorKey is not None:
        image = image.convert()
        if colorKey == -1:
            colorKey = image.get_at((0, 0))
        image.set_colorkey(colorKey)
    else:
        image = image.convert_alpha()
    return image


def load_level(filename):
    filename = "Data/levels/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    return level_map


def generate_level(level, game):
    new_player, x, y = None, None, None
    new_level = []
    for y in range(len(level)):
        new_level.append([])
        new_level[-1] = [0] * len(level[y])
        for x in range(len(level[y])):
            if level[y][x] == '.':
                new_level[y][x] = Floor('empty', x, y, game)
            elif level[y][x] == '#':
                new_level[y][x] = Wall('wall', x, y, game)
            elif level[y][x] == '%':
                new_level[y][x] = Door('door', x, y, game, True)
            elif level[y][x] == 'K':
                new_level[y][x] = Key('key', x, y, game)
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '@':
                new_level[y][x] = Floor('empty', x, y, game)
                new_player = Player('player', x, y, game)
    # вернем игрока, а также размер поля в клетках
    return new_level, new_player, x, y


def print_text(screen, x, y, size, _str, color):
    text = pygame.font.SysFont("monospace", size)
    string = text.render(str(_str), 0, color)
    screen.blit(string, (x, y))