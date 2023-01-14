import pygame
import json


class Settings:
    def __init__(self):
        self.bindsKeyBoard = {'up': [pygame.K_UP],
                              'down': [pygame.K_DOWN],
                              'right': [pygame.K_RIGHT],
                              'left': [pygame.K_LEFT],
                              'interact': [pygame.K_e]}

        self.bindsJoystick = {'interact': [0, 5]}
        with open('Data/settings.json', 'r') as file:
            data = json.load(file)
            self.isSound = data['sound']
            self.bindsKeyBoard = data['binds']['keyBoard']
            self.bindsJoystick = data['binds']['joystick']

    def updateKey(self, key, value, isJoystick):
        if isJoystick:
            self.bindsJoystick[key] = value
        else:
            self.bindsKeyBoard[key] = value

    def save(self, mx):
        data = {"binds": {"keyBoard": {"up": self.bindsKeyBoard['up'],
                                       "down": self.bindsKeyBoard['down'],
                                       "right": self.bindsKeyBoard['right'],
                                       "left": self.bindsKeyBoard['left'],
                                       "interact": self.bindsKeyBoard['interact']},
                          "joystick": {"interact": self.bindsJoystick['interact']}},
                'sound': all(mx.mixer.getVolume())}
        with open('Data/settings.json', 'w') as file:
            json.dump(data, file)
