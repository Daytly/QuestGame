import pygame
import os


class Mixer:
    def __init__(self, path):
        self.sounds = {}
        for sound in os.listdir(path):
            self.sounds[sound.split('.')[0]] = pygame.mixer.Sound(f'{path}/{sound}')

    def play(self, name, loops=-1, fade_ms=0):
        if name in self.sounds:
            self.sounds[name].play(loops=loops, fade_ms=fade_ms)
            print(f'Play {name}')
            return True
        return False

    def stop(self, name):
        if name in self.sounds:
            self.sounds[name].stop()
            return True
        return False


mixer = Mixer('Data/sounds')
