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

        self.reset_stats()

    def reset_stats(self):
        """ reset the game stats """
        self.level = 1
        self.lives_left = self.player_life_limit
