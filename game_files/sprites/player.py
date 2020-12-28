import pygame
import os
from pygame.sprite import Sprite


class Player(Sprite):
    """ player sprite class """

    def __init__(self, bullfrog):
        # initialize the inherited variables
        super().__init__()
        self.screen = bullfrog.screen
        self.settings = bullfrog.settings

        self.screen_rect = bullfrog.screen.get_rect()
        self._load_player_image()
        # get rect
        self.rect = self.image.get_rect()

        self.movement_speed = 4.0

        # set player initial position
        self.rect.midbottom = self.screen_rect.midbottom
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.moving_left = False
        self.moving_right = False

    def _load_player_image(self):
        """ Load player image from assets folder """
        # set player image
        path = os.path.dirname(__file__)
        self.image = pygame.image.load(
            os.path.join(path, 'sprite_images/player_ship.png'))

    def reset_player(self):
        """ reset player position """
        # set player initial position
        self.rect.midbottom = self.screen_rect.midbottom
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def check_position(self):
        """ check that the player position is in bounds """
        if self.rect.top < 31:
            return True
        else:
            return False

    def update_position(self):
        if self.rect.left > 0 and self.moving_left:
            self._move_left()
        elif self.rect.right < self.settings.screen_width and self.moving_right:
            self._move_right()

    def move_forward(self):
        """ move player forward """
        self.y -= self.settings.screen_rows
        self.rect.y = self.y

    def move_backward(self):
        """ move player backward """
        if self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.screen_rows
        self.rect.y = self.y

    def _move_left(self):
        self.x -= self.movement_speed
        self.rect.x = self.x

    def _move_right(self):
        self.x += self.movement_speed
        self.rect.x = self.x
