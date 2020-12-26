import pygame.font
from pygame import Surface


class Button(Surface):
    """ create a button """

    def __init__(self, surface, button_text: str):
        """ initialize button settings """
        self.width, self.height = 150, 50
        super(Button, self).__init__((self.width, self.height))

        self.button_color = (84, 136, 165)
        self.text_color = (16, 27, 33)
        # coords to set button to middle of screen
        self.button_mid_pos_x = (
            surface.width/2)-(self.width/2)
        self.button_mid_pos_y = (surface.height/3)*2

        self.font = pygame.font.SysFont(None, 48, bold=True)

        # build the button rect and set it's position
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x, self.rect.y = self.button_mid_pos_x, self.button_mid_pos_y

        self._prep_msg(button_text)

        self.fill(self.button_color)

    def check_button(self, mouse_pos):
        """ check for button collision """
        if self.rect.collidepoint(mouse_pos):
            return True
        return False

    def set_position(self, x_pos=None, y_pos=None):
        """ Set the position of the button """
        if x_pos:
            self.rect.x = x_pos
        if y_pos:
            self.rect.y = y_pos

        self.msg_image_rect.center = self.rect.center

    def _prep_msg(self, text: str):
        """ prep the text to be rendered in the button """
        self.msg_image = self.font.render(
            text, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
