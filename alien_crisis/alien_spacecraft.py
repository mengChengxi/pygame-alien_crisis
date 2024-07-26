import pygame
from game_settings import Game_settings
import random
from spacecraft import Spacecraft


class Alien:

    def __init__(self, spacecraft_settings, screen_rect, imagePath):
        self.spacecraft_settings = spacecraft_settings

        self.image = pygame.image.load(imagePath)

        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()





        self.screen_rect = screen_rect
        self.game_settings = Game_settings()
        edge = random.randint(0, 3)
        if edge == 0:
            self.x = random.randint(0, self.game_settings.screen_width)
            self.y = 0
        elif edge == 1:
            self.x = random.randint(0, self.game_settings.screen_width)
            self.y = self.game_settings.screen_height
        elif edge == 2:
            self.x = 0
            self.y = random.randint(0, self.game_settings.screen_height)
        elif edge == 3:
            self.x = self.game_settings.screen_width
            self.y = random.randint(0, self.game_settings.screen_height)

        self.game_settings.screen_width
        # self.x=screen_rect.centerx
        # self.y=screen_rect.centery

        self.rect.centerx = self.x
        self.rect.centery = self.y

        self.vx = 0
        self.vy = 0
        self.v = self.game_settings.alien_speed

    def move(self, spacecraft):
        self.vx = self.v * (spacecraft.x - self.x)
        self.vy = self.v * (spacecraft.y - self.y)

        self.x += self.vx
        self.y += self.vy

        self.rect.centerx = self.x
        self.rect.centery = self.y

    def draw(self, screen):
        # print(self)
        screen.blit(self.image, self.rect)
