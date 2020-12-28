from pygame.sprite import Sprite
import os
import pygame


class Laser(Sprite):
    def __init__(self, x_y_dir: list):
        """
            Inputs: x_y_dir: list [x, y, direction(1, -1)]
        """
        super().__init__()

        self.image = pygame.image.load(os.path.join(
            os.path.dirname(__file__), "sprite_images/laser.png"))

        self.rect = self.image.get_rect()
        self.rect.x = x_y_dir[0] + 16
        self.rect.y = x_y_dir[1] + 16
        self.firing_speed = 25
        self.firing_direction = x_y_dir[2]
        self._rotate_image(90)

    def _rotate_image(self, rotation: float):
        rotated_image = pygame.transform.rotate(self.image, rotation)
        rotated_rect = rotated_image.get_rect(
            center=self.image.get_rect(center=(self.rect.x, self.rect.y)).center)
        self.image = rotated_image
        self.rect = rotated_rect

    def update(self):
        self.rect.x += self.firing_speed * self.firing_direction
