import pygame
import os
import random
from pygame.sprite import Sprite


class Gnat(Sprite):

    def __init__(self, screen_dim: tuple):
        """
            Input: screen_dim: tuple (width, height)
        """
        super().__init__()
        x_pos_right = screen_dim[0]-32
        self.positions_list: list = [
            (10, 465), (10, 365), (10, 265), (10, 165), (10, 65),  # left side 90
            (x_pos_right, 465), (x_pos_right, 365), (x_pos_right, 265),
            (x_pos_right, 165), (x_pos_right, 65)
        ]
        self.random_position = random.randint(0, 9)
        self._load_gnat_image()
        self._rotate_image(self._get_angle(self.random_position))

        self._set_position(self.random_position)

    def get_direction(self):
        """
            return 1 if the gnat is facing right
            return -1 if the gnat is facing left
        """
        if self.random_position <= 4:
            return 1
        else:
            return -1

    def get_position(self):
        return [self.positions_list[self.random_position]]

    def _get_angle(self, random_int: int):
        if self.random_position <= 4:
            return 90.0
        else:
            return 270.0
        return 0

    def _set_position(self, random_position):
        self.rect.x = self.positions_list[random_position][0]
        self.rect.y = self.positions_list[random_position][1]

        self.x, self.y = self.rect.x, self.rect.y

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
