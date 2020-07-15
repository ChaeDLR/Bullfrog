class GameStats:
	""" track and control game stats """

	def __init__(self, frogger):
		""" initialize game stats """
		self.settings = frogger.settings

		self.game_active = False
		self.high_score = 0

		self.reset_stats()

	def reset_stats(self):
		""" reset the game stats """
		self.level = 1
		self.lives_left = self.settings.player_life_limit