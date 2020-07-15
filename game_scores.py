import pygame.font

class Scoreboard:
	""" Store and report scoring info """

	def __init__(self, frogger):
		""" initialize scoring attributes """
		self.frogger = frogger
		self.screen = frogger.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = frogger.settings
		self.stats = frogger.stats
		
		# text settings
		self.text_color = (0, 51, 25)
		self.text_font = pygame.font.SysFont(None, 38)

		self.prep_level()
		self.prep_lives()

	def prep_level(self):
		""" make level into an image """
		level_string = 'Level: {:,}'.format(self.stats.level)
		self.level_image = self.text_font.render(
			level_string, True, self.text_color, self.settings.bg_color)
		# Position the rendered text
		self.level_rect = self.level_image.get_rect()
		self.level_rect.left = self.screen_rect.left + 20
		self.level_rect.top = 20
	
	def prep_lives(self):
		""" makes player lives into image """
		player_lives = 'Lives: {}'.format(self.stats.lives_left)
		self.lives_image = self.text_font.render(
			player_lives, True, self.text_color, self.settings.bg_color)
		# position rendered text
		self.player_lives_rect = self.level_image.get_rect()
		self.player_lives_rect.right = self.screen_rect.right - 20
		self.player_lives_rect.top = 20

	def show_score(self):
		""" display current information to the screen """
		self.screen.blit(self.level_image, self.level_rect)
		self.screen.blit(self.lives_image, self.player_lives_rect)