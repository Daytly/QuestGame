import pygame
import json


class Settings:
    def __init__(self):
        self.bindsKeyBoard = {'up': pygame.K_UP,
                              'down': pygame.K_DOWN,
                              'right': pygame.K_RIGHT,
                              'left': pygame.K_LEFT,
                              'interact': pygame.K_e,
                              'menu': pygame.K_ESCAPE}

        self.bindsJoystick = {'interact': 0,
                              'menu': 7,
                              'up': pygame.K_UP,
                              'down': pygame.K_DOWN,
                              'right': pygame.K_RIGHT,
                              'left': pygame.K_LEFT,
                              'exit': 5}
        with open('Data/settings.json', 'r') as file:
            data = json.load(file)
            self.isSound = data['sound']
            for key in data['binds']['keyBoard'].keys():
                self.bindsKeyBoard[key] = data['binds']['keyBoard'][key]
            for key in data['binds']['joystick'].keys():
                self.bindsJoystick[key] = data['binds']['joystick'][key]

    def updateKey(self, key, value, isJoystick):
        if isJoystick:
            self.bindsJoystick[key] = value
        else:
            self.bindsKeyBoard[key] = value

    def save(self, mx):
        data = {"binds": {"keyBoard": {'up': self.bindsKeyBoard['up'],
                                       'down': self.bindsKeyBoard['down'],
                                       'right': self.bindsKeyBoard['right'],
                                       'left': self.bindsKeyBoard['left'],
                                       'interact': self.bindsKeyBoard['interact'],
                                       'menu': self.bindsKeyBoard['menu']},
                          "joystick": {'up': self.bindsJoystick['up'],
                                       'down': self.bindsJoystick['down'],
                                       'right': self.bindsJoystick['right'],
                                       'left': self.bindsJoystick['left'],
                                       "interact": self.bindsJoystick['interact'],
                                       'menu': self.bindsJoystick['menu'],
                                       'exit': self.bindsJoystick['exit']}},
                'sound': all(mx.mixer.getVolume())}
        self.isSound = data['sound']
        with open('Data/settings.json', 'w') as file:
            json.dump(data, file)
