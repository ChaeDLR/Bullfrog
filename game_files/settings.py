import random


class Settings:
    """ organize our game settings """

    def __init__(self):
        """ initialize our game settings """
        self.change_bg_color()
        self.screen_width = 400
        self.screen_height = 600

        self.direction_list = [1, -1]

        self.screen_rows = self.screen_height / 12

        # enemy random variables
        self.enemy_speed = random.randint(1, 3)
        self.enemy_direction = 1

        # player stats
        self.player_life_limit = 3

    def change_bg_color(self):
        self.bg_color = (random.randint(1, 255), random.randint(
            1, 255), random.randint(1, 255))
