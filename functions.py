import os
import random

import pygame
from player import Player
from wall import Wall
from floor import Floor
from door import Door
from key import Key
from slime import Slime
from detail import Detail
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


def generate_levelInHouse(level, game):
    new_player, x, y = None, None, None
    new_level = []
    enemy = []
    for y in range(len(level)):
        new_level.append([])
        new_level[-1] = [0] * len(level[y])
        for x in range(len(level[y])):
            if x == y == 0:
                new_level[y][x] = Floor('empty', x, y, game, 3, 3, 0)
            elif x == len(level[y]) - 1 and y == 0:
                new_level[y][x] = Floor('empty', x, y, game, 3, 3, 2)
            elif x == 0 and y == len(level) - 1:
                new_level[y][x] = Floor('empty', x, y, game, 3, 3, 6)
            elif x == len(level[y]) - 1 and y == len(level) - 1:
                new_level[y][x] = Floor('empty', x, y, game, 3, 3, 8)
            elif x == 0:
                new_level[y][x] = Floor('empty', x, y, game, 3, 3, 3)
            elif x == len(level[y]) - 1:
                new_level[y][x] = Floor('empty', x, y, game, 3, 3, 5)
            elif y == 0:
                new_level[y][x] = Floor('empty', x, y, game, 3, 3, 1)
            elif y == len(level) - 1:
                new_level[y][x] = Floor('empty', x, y, game, 3, 3, 7)
            else:
                new_level[y][x] = Floor('empty', x, y, game, 3, 3, 4)
            if level[y][x] == '#':
                new_level[y][x] = Wall('wall', x, y, game, 2, 1)
            elif level[y][x] == '%':
                new_level[y][x] = Door('door', x, y, game, True, 1, 1)
            elif level[y][x] == 'K':
                new_level[y][x] = Key('key', x, y, game, 1, 1)
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '@':
                new_player = Player('player', x, y, game)
            elif level[y][x] == '-':
                enemy.append(Slime('slime', x, y, game, True, 1, 1))

    # вернем игрока, а также размер поля в клетках
    return new_level, new_player, enemy, x, y


def generate_levelOutside(level, game):
    new_player, x, y = None, None, None
    new_level = []
    enemy = []
    for y in range(len(level)):
        new_level.append([])
        new_level[-1] = [0] * len(level[y])
        for x in range(len(level[y])):
            if x == y == 0:
                new_level[y][x] = Floor('grass', x, y, game, 2, 2, 0)
            elif x == len(level[y]) - 1 and y == 0:
                new_level[y][x] = Floor('grass', x, y, game, 2, 2, 2)
            elif x == 0 and y == len(level) - 1:
                new_level[y][x] = Floor('grass', x, y, game, 2, 2, 6)
            elif x == len(level[y]) - 1 and y == len(level) - 1:
                new_level[y][x] = Floor('grass', x, y, game, 2, 2, 8)
            elif x == 0:
                new_level[y][x] = Floor('grass', x, y, game, 2, 2, 3)
            elif x == len(level[y]) - 1:
                new_level[y][x] = Floor('grass', x, y, game, 2, 2, 5)
            elif y == 0:
                new_level[y][x] = Floor('grass', x, y, game, 2, 2, 1)
            elif y == len(level) - 1:
                new_level[y][x] = Floor('grass', x, y, game, 2, 2, 7)
            else:
                new_level[y][x] = Floor('grass', x, y, game, 2, 2, 4)
            if level[y][x] == '.':
                if random.randrange(5) == 0:
                    Detail('floorDetail', x, y, game, 16, 4, random.randrange(48))
            elif level[y][x] == '#':
                new_level[y][x] = Wall('wall', x, y, game, 2, 1)
            elif level[y][x] == '%':
                new_level[y][x] = Door('door', x, y, game, True, 1, 1)
            elif level[y][x] == 'K':
                new_level[y][x] = Key('key', x, y, game, 1, 1)
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '@':
                new_player = Player('player', x, y, game)
            elif level[y][x] == '-':
                enemy.append(Slime('slime', x, y, game, True, 1, 1))

    # вернем игрока, а также размер поля в клетках
    return new_level, new_player, enemy, x, y


def print_text(screen, x, y, size, _str, color):
    text = pygame.font.SysFont("monospace", size)
    string = text.render(str(_str), 0, color)
    screen.blit(string, (x, y))
