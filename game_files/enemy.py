import pygame
import os
import random
from pygame.sprite import Sprite


class Enemy(Sprite):
    """ enemy class """

    def __init__(self, bullfrog, row_number):
        """ initialize enemy """
        super().__init__()
        self.screen = bullfrog.screen
        self.settings = bullfrog.settings
        self._load_enemy_image()
        # enemy rect
        self.rect = self.image.get_rect()
        self.enemy_direction = random.choice((-1, 1))
        self.screen_rect = self.screen.get_rect()
        self.enemy_speed = random.randint(3, 8)
        self.x = float(self.rect.x)
        self.rect.y = row_number * 100

    def _load_enemy_image(self):
        path = os.path.dirname(__file__)
        self.image = pygame.image.load(
            os.path.join(path, 'assets/enemy_ship.png'))

    def check_edges(self):
        """ make sure player is in screen bounds """
        if self.rect.right >= self.screen_rect.right:
            self.enemy_direction = -1
        elif self.rect.left <= 0:
            self.enemy_direction = 1

    def update(self):
        """ update the enemy position """
        self.x += self.enemy_speed * self.enemy_direction
        self.rect.x = self.x
