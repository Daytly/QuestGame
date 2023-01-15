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
from tree import Tree
from spikes import Spikes
from darkNinja import DarkNinja
from missile import Missile
from portal import Portal
import settings
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

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, 'T'), level_map))


def generate_level(level, game, inHouse):
    new_player, x, y = None, None, None
    new_level = []
    enemy = []
    spikesCoord = []
    closed = False
    tilesFloor = 'empty' if inHouse else 'grass'
    level = ['T' * 18] * 8 + level + ['T' * 18] * 8
    for y in range(len(level)):
        level[y] = 'T' * 9 + level[y] + 'T' * 9
        for x in range(len(level[y])):
            if level[y][x] == 'K':
                closed = True
    for y in range(len(level)):
        new_level.append([])
        new_level[-1] = [0] * len(level[y])
        for x in range(len(level[y])):
            # Генерация карты
            if x == y == 0:
                new_level[y][x] = Floor(tilesFloor, x, y, game, 2, 2, 0)
            elif x == len(level[y]) - 1 and y == 0:
                new_level[y][x] = Floor(tilesFloor, x, y, game, 2, 2, 2)
            elif x == 0 and y == len(level) - 1:
                new_level[y][x] = Floor(tilesFloor, x, y, game, 2, 2, 6)
            elif x == len(level[y]) - 1 and y == len(level) - 1:
                new_level[y][x] = Floor(tilesFloor, x, y, game, 2, 2, 8)
            elif x == 0:
                new_level[y][x] = Floor(tilesFloor, x, y, game, 2, 2, 3)
            elif x == len(level[y]) - 1:
                new_level[y][x] = Floor(tilesFloor, x, y, game, 2, 2, 5)
            elif y == 0:
                new_level[y][x] = Floor(tilesFloor, x, y, game, 2, 2, 1)
            elif y == len(level) - 1:
                new_level[y][x] = Floor(tilesFloor, x, y, game, 2, 2, 7)
            else:
                new_level[y][x] = Floor(tilesFloor, x, y, game, 2, 2, 4)

            if level[y][x] == '.':
                if random.randrange(5) == 0:
                    Detail('floorDetail', x, y, game, 16, 4, random.randrange(48))
            elif level[y][x] == '#':
                new_level[y][x] = Wall('wall', x, y, game, 2, 1, random.randrange(2))
            elif level[y][x] == '%':
                new_level[y][x] = Door('door', x, y, game, closed, 1, 1)
            elif level[y][x] == 'K':
                new_level[y][x] = Key('key', x, y, game, 2, 1)
            elif level[y][x] == 'T':
                new_level[y][x] = Tree('tree', x, y, game, 1, 1)
            elif level[y][x] == '$':
                new_level[y][x] = Spikes('spikes', x, y, game, 10, 1)
                spikesCoord.append([y, x])
            elif level[y][x] == 'L':
                new_level[y][x] = Portal('ladder', x, y, game, 1, 1)
                game.ladders_group.add(new_level[y][x])
    # Генерация врагов
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '|':
                enemy.append(Slime('slime', x, y, game, True, 4, 1))
            elif level[y][x] == '-':
                enemy.append(Slime('slime', x, y, game, False, 4, 1))
            elif level[y][x] == '^':
                enemy.append(DarkNinja('darkNinja', x, y, game, 4, 2, True))
            elif level[y][x] == '>':
                enemy.append(DarkNinja('darkNinja', x, y, game, 4, 2, False))
    # Генерация игрока
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '@':
                new_player = Player('player', x, y, game)

    # вернем игрока, а также размер поля в клетках
    return new_level, new_player, enemy, spikesCoord, x, y
