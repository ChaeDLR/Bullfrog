import pygame
import os
import random
from pygame.sprite import Sprite


class Gnat(Sprite):

    def __init__(self):
        """ gnat enemy sprite """
        super().__init__()
        self.positions_list: list = [
            (10, 465), (10, 365), (10, 265), (10, 165), (10, 65)]
        self.random_position = random.randint(0, 4)
        self._load_gnat_image()
        self._rotate_image(self._get_angle(self.random_position))

        self._set_position(self.random_position)

    def get_position(self):
        return [self.positions_list[self.random_position]]

    def _get_angle(self, random_int: int):
        if self.random_position <= 4:
            return 90.0
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
        self.image = pygame.image.load(os.path.join(path, 'assets/gnat.png'))
        self.rect = self.image.get_rect()
