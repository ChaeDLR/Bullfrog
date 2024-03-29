import pygame
import os
import random
from pygame.sprite import Sprite


class Gnat(Sprite):

    def __init__(self, screen_dim: tuple, mode=0):
        """
            Input: screen_dim: tuple (width, height)
        """
        super().__init__()
        x_pos_right = screen_dim[0]-32
        self.screen_width, self.screen_height = screen_dim
        self.row = self.screen_height/7-12

        self._load_gnat_image()
        self._load_positions(x_pos_right, mode)
        self._rotate_image(self._get_angle(self.random_position))
        self._set_position(self.random_position)
        self.time_born = pygame.time.get_ticks()

    def check_life_length(self):
        """
            Return true if it should still exist
            return false if it should be deleted
        """
        if (pygame.time.get_ticks()-self.time_born) < 1000:
            return True
        return False

    def _load_positions(self, x_pos_right: int, mode=0):
        if mode == 0:
            self.positions_list: list = [
                # left side| 90 degree
                (10, self.row*5+15), (10, self.row*4), (10, self.row * 3),
                (10, self.row*2), (10, self.row),

                (x_pos_right, self.row*5+15), (x_pos_right, self.row*4),
                (x_pos_right, self.row*3), (x_pos_right, self.row*2),
                (x_pos_right, self.row)
            ]
        elif mode == 1:
            self.positions_list: list = [
                # left side| 90 degree
                (10, self.row*5+15), (10, self.row*4), (10, self.row * 3),
                (10, self.row*2),

                (x_pos_right, self.row*5+15), (x_pos_right, self.row*4),
                (x_pos_right, self.row*3), (x_pos_right, self.row*2),
            ]

        self.random_position = random.randint(0, len(self.positions_list)-1)

    def get_direction(self):
        """
            return 1 if the gnat is facing right
            return -1 if the gnat is facing left
        """
        if self.random_position <= len(self.positions_list)/2-1:
            return 1
        else:
            return -1

    def _get_angle(self, random_int: int):
        """
            Passed to _rotate_image to set the direction the png should face
        """
        if self.random_position <= len(self.positions_list)/2-1:
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
