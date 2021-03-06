import pygame
import os
import random
from pygame.sprite import Sprite


class Enemy(Sprite):
    """ enemy class """

    def __init__(self, screen_w_h: tuple, row_number: int):
        """ screen_w: (screen_width: int)
            row_number: ()
        """
        super().__init__()
        self._load_enemy_image()
        self.screen_width, self.screen_height = screen_w_h
        self.rect = self.image.get_rect()
        self.enemy_direction = random.choice((-1, 1))
        self.enemy_speed = random.randint(3, 9)
        self._set_enemy_spawn(row_number)

    def set_enemy_speed(self, speed_modifier: int):
        self.enemy_speed = random.randint(
            3 + speed_modifier, 9 + speed_modifier
            )

    def _set_enemy_spawn(self, row: int):
        self.x = float(self.rect.x + (
            random.randint(5, self.screen_width-40)))
        self.rect.x = self.x
        self.rect.y = (self.screen_height/7)*row

    def _load_enemy_image(self):
        path = os.path.dirname(__file__)
        self.image = pygame.image.load(
            os.path.join(path, 'sprite_images/enemy_ship.png'))

    def change_direction(self):
        self.enemy_direction = self.enemy_direction * -1

    def check_edges(self):
        """ make sure player is in screen bounds """
        if self.rect.right >= self.screen_width:
            self.enemy_direction = -1
        elif self.rect.left <= 0:
            self.enemy_direction = 1

    def update(self):
        """ update the enemy position """
        self.x += self.enemy_speed * self.enemy_direction
        self.rect.x = self.x
