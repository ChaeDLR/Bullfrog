class GameStats:
    """ track and control game stats """

    def __init__(self):
        """ initialize game stats """
        self.player_life_limit = 3
        self.game_active = False
        self.high_score = 0

        self.active_level = 0

        self.game_over = False
        self.game_paused = False
        self.settings_menu_active = False
        self.main_menu_active = True

        self.reset_stats()
    
    def set_active_screen(self, game_over=False, game_paused=False, settings_menu=False, main_menu=False, game_active=False):
        self.game_active = game_active
        self.game_over = game_over
        self.game_paused = game_paused
        self.settings_menu_active = settings_menu
        self.main_menu_active = main_menu

    def reset_stats(self):
        """ reset the game stats """
        self.level = 1
        self.lives_left = self.player_life_limit
