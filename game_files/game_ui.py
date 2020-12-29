import pygame.font
from pygame.sprite import Group
from .sprites.player import Player


class Game_Ui:
    """ Displays game ui to surface """

    def __init__(self, surface, settings, stats):
        """ initialize scoring attributes """
        self.screen = surface
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.stats = stats
        self.rect = self.screen_rect

        # text settings
        self.text_color = (0, 51, 25)
        self.text_font = pygame.font.SysFont(None, 38)

        self.update_level()
        self.update_lives()

    def update_level(self):
        """ make level into an image """
        level_string = 'Level: {:,}'.format(self.stats.level)
        self.level_image = self.text_font.render(
            level_string, True, self.text_color, self.settings.bg_color)
        # Position the rendered text
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.screen_rect.left + 20
        self.level_rect.top = 20

    def update_lives(self):
        """ makes player lives into image """
        self.ships = Group()
        for life_number in range(self.stats.lives_left):
            ship = Player(self)
            ship.rect.x = self.screen_rect.width - \
                40 - (life_number * ship.rect.width)
            ship.rect.y = 10
            self.ships.add(ship)

    def display_ui(self):
        """ display current information to the screen """
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
