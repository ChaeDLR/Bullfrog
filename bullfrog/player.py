import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    """ player class """

    def __init__(self, frogger):
        """ initialize player """

        # initialize the inherited variables
        super().__init__()

        self.screen = frogger.screen
        self.settings = frogger.settings

        self.screen_rect = frogger.screen.get_rect()

        # set player image
        self.image = pygame.image.load('../assets/player_ship.png')
        # get rect
        self.rect = self.image.get_rect()

        # set player initial position
        self.rect.midbottom = self.screen_rect.midbottom
        self.y = float(self.rect.y)

    def reset_player(self):
        """ reset player position """
        # set player initial position
        self.rect.midbottom = self.screen_rect.midbottom
        self.y = float(self.rect.y)

    def check_position(self):
        """ check player position """
        if self.rect.top < 0:
            return True

    def move_forward(self):
        """ move player forward """
        self.y -= self.settings.screen_rows
        self.rect.y = self.y

    def move_backward(self):
        """ move player backward """
        if self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.screen_rows
        self.rect.y = self.y

    def blitme(self):
        """ blit the player """
        self.screen.blit(self.image, self.rect)
