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

        self.screen_rows = self.screen_height / 12

        self.player_life_limit = 3

        self.reset_background()

    def reset_background(self):
        self.rgb_color = [0, 250, 0]
        self.bg_color = (self.rgb_color[0],
                         self.rgb_color[1], self.rgb_color[2])

    def change_bg_color(self):
        """ Starts on green makes its way to red as the player beats levels """
        if self.rgb_color[2] < 250 and self.rgb_color[1] == 250:
            self.rgb_color[2] += 50
        elif self.rgb_color[2] == 250 and self.rgb_color[1] > 0:
            self.rgb_color[1] -= 50
        elif self.rgb_color[1] == 0 and self.rgb_color[0] < 250:
            self.rgb_color[0] += 50
        elif self.rgb_color[0] == 250 and self.rgb_color[2] > 0:
            self.rgb_color[2] -= 50
        else:
            self.rgb_color = [0, 250, 0]

        self.bg_color = (self.rgb_color[0],
                         self.rgb_color[1], self.rgb_color[2])
