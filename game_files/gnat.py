import pygame
import os
import random
from pygame.sprite import Sprite


class Gnat(Sprite):

    def __init__(self, bullfrog):
        """ gnat enemy sprite """
        super().__init__()
        self.screen = bullfrog.screen
        self.settings = bullfrog.settings
        self.positions_list: list = [(10, 450)]
        random_position = 0  # random.randint(0, 1)
        self._load_gnat_image()
        self._rotate_image(self._get_angle(random_position))

        self._set_position(random_position)

    def _get_angle(self, random_int: int):
        if random_int < 2:
            return 90.0

    def _set_position(self, random_position):
        self.rect.x = self.positions_list[random_position][0]
        self.rect.y = self.positions_list[random_position][1]

    def _rotate_image(self, rotation: float):
        self.rotated_image = pygame.transform.rotate(self.image, rotation)
        self.rotated_rect = self.rotated_image.get_rect(
            center=self.image.get_rect(center=(self.rect.x, self.rect.y)).center)
        self.image = self.rotated_image
        self.rect = self.rotated_rect

    def _load_gnat_image(self):
        path = os.path.dirname(__file__)
        self.image = pygame.image.load(os.path.join(path, 'assets/gnat.png'))
        self.rect = self.image.get_rect()
