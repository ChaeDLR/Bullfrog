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

	def prep_level(self):
		""" make level into an image """
		level_string = 'Level: {:,}'.format(self.stats.level)
		self.level_image = self.text_font.render(
			level_string, True, self.text_color, self.settings.bg_color)
		# Position the rendered text
		self.level_rect = self.level_image.get_rect()
		self.level_rect.left = self.screen_rect.left + 20
		self.level_rect.top = 20

	def show_score(self):
		""" display current information to the screen """
		self.screen.blit(self.level_image, self.level_rect)