import pygame.font
class Button:
	""" create a button """
	def __init__(self, frogger):
		""" initialize button settings """
		self.screen = frogger.screen
		self.screen_rect = self.screen.get_rect()

		# propeties of the button
		self.width, self.height = 150, 50
		self.button_color = (84, 136, 165)
		self.text_color = (16, 27, 33)
		self.font = pygame.font.SysFont(None, 48, bold=True)

		# build the button rect and set it's position
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		self._prep_msg()
	
	def _prep_msg(self):
		""" prep the text to be rendered in the button """
		self.msg_image = self.font.render("Play", True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		""" draw button to the screen """
		# draw empty button to the screen
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
