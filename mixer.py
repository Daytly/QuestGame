import pygame
import os
pygame.init()


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

    def setVolume(self, name, value):
        if name in self.sounds:
            self.sounds[name].set_volume(value)
            return True
        return False

    def volume(self):
        for sound in self.sounds.values():
            sound.set_volume(0 if sound.get_volume() else 1)

    def getVolume(self):
        return [i.get_volume() for i in self.sounds.values()]


mixer = Mixer('Data/sounds')
