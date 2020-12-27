import random


class Settings:
    """ organize our game settings """

    def __init__(self):
        """ initialize our game settings """
        self.screen_width = 400
        self.screen_height = 600

        self.screen_mid_x = (self.screen_width/2)
        self.screen_mid_y = (self.screen_height/2)

        self.direction_list = [1, -1]

        self.bg_color = (113, 143, 30)

        self.screen_rows = self.screen_height / 12

        self.player_life_limit = 3
