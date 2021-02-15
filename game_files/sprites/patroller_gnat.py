import pygame
import os
import random
from pygame.sprite import Sprite


class PatrollerGnat(Sprite):

    def __init__(self, screen_dim: tuple):
        """
            screen_dim: tuple (width, height)
            Enemy class that moves like a patroller but also shoots lasers
        """
        super().__init__()
        self.screen_width, self.screen_height = screen_dim
        self.direction = random.choice((-1, 1))
        self.speed = random.randint(3, 8)

        self._load_gnat_image()
        self._set_enemy_spawn()

    def _set_enemy_spawn(self):
        self.x = float(self.rect.x + (
            random.randint(5, self.screen_width-40)))
        self.rect.x = self.x
        self.rect.y = (self.screen_height/7)+5

    def _rotate_image(self, rotation: float):
        rotated_image = pygame.transform.rotate(self.image, rotation)
        rotated_rect = rotated_image.get_rect(
            center=self.image.get_rect(center=(self.rect.x, self.rect.y)).center)
        self.image = rotated_image
        self.rect = rotated_rect

    def _load_gnat_image(self):
        path = os.path.dirname(__file__)
        self.image = pygame.image.load(
            os.path.join(path, 'sprite_images/gnat.png'))
        self.rect = self.image.get_rect()

    def _check_edges(self):
        """ Make sure the sprite stays in the screen bounds """
        if self.rect.right >= self.screen_width:
            self.direction = -1
        elif self.rect.left <= 0:
            self.direction = 1

    def update(self):
        """ update gnat position """
        self._check_edges()
        self.x += self.speed * self.direction
        self.rect.x = self.x
