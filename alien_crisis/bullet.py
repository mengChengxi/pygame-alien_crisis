import pygame
import game_settings


class Bullet:

    def __init__(self, x, y, direction, screen):

        self.x = x
        self.y = y
        self.direction = direction
        self.face = pygame.Surface((10, 10), flags=pygame.HWSURFACE)
        # 填充颜色
        self.face.fill(color="red")

    def draw_bullet(self, screen):
        screen.blit(self.face, (self.x, self.y))

    def move(self):

        if self.direction == 1:
            self.y -= 2
        if self.direction == 2:
            self.x -= 2
        if self.direction == 3:
            self.y += 2
        if self.direction == 4:
            self.x += 2
