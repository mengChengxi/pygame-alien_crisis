import pygame
from game_settings import Game_settings
from bullet import Bullet
import math


class Spacecraft:

    def __init__(self, spacecraft_settings, screen_rect, imagePath):
        self.spacecraft_settings = spacecraft_settings

        self.image = pygame.image.load(imagePath)

        self.image = pygame.transform.scale(self.image, (30, 30))

        self.rect = self.image.get_rect()
        self.screen_rect = screen_rect
        self.game_settings = Game_settings()
        self.currentdirection = 0

        self.x = screen_rect.centerx
        self.y = screen_rect.centery

        self.vx = 0
        self.vy = 0

        self.ax = 0
        self.ay = 0

        self.acceleration = 0.001
        self.friction = 0.01
        self.bullet = []

    def move(self, screen, mx, my):
        if self.vy > 0:
            self.vy -= self.vy**2 * self.friction
        if self.vx > 0:
            self.vx -= self.vx**2 * self.friction

        self.x += self.vx
        self.y += self.vy

        if mx != -1 and my != -1:
            self.ax = self.acceleration * (mx - self.x)
            self.ay = self.acceleration * (my - self.y)

            self.vx += self.ax
            self.vy += self.ay

        self.rect.centerx = self.x
        self.rect.centery = self.y

        # self.rotate()

    def fire(self, screen, direction_a, count):

        for i in range(len(direction_a)):
            if direction_a[i] == 1:
                direction = i + 1
                if (
                    count % self.game_settings.bullet_speed_factor == 0
                    and len(self.bullet) < self.game_settings.bullet_limit
                ):
                    self.bullet.append(Bullet(self.x, self.y, direction, screen))

        for i in self.bullet:
            if (
                i.x > self.game_settings.screen_width
                or i.x < 0
                or i.y < 0
                or i.y > self.game_settings.screen_height
            ):
                self.bullet.remove(i)
            i.move()

    def draw(self, screen):

        screen.blit(self.image, self.rect)
        for i in self.bullet:
            i.draw_bullet(screen)

    def test(self, Alien):
        for i in self.bullet:
            if (i.x - Alien.x) ** 2 < 100 and (i.y - Alien.y) ** 2 < 100:
                return True

    def testcollide(self, Alien):
        if (Alien.x - self.x) ** 2 < 100 and (Alien.y - self.y) ** 2 < 100:
            return True

    def rotate(self):
        self.image = pygame.transform.rotate(self.image, -self.currentdirection)
        if self.vy == 0:
            self.vy += 0.1
        if self.vx > 0:

            self.currentdirection = (
                math.pi * math.atan(self.vx / self.vy) / math.pi * 180
            )
        else:
            self.currentdirection = -math.atan(self.vx / self.vy) / math.pi * 180
        self.image = pygame.transform.rotate(self.image, self.currentdirection)
