import pygame.font
from pygame import Surface
from .button import Button
from ..colors import dark_teal, orange


class PauseMenu(Surface):

    def __init__(self, width: int, height: int):
        super(PauseMenu, self).__init__((width, height))
        self.background_color = dark_teal
        self.text_color = orange
        self.font = pygame.font.SysFont(None, 50)
        self.rect = pygame.Rect(0, 0, width, height)

        self.width, self.height = width, height

        self._load_buttons()
        self._load_text()

    def _load_buttons(self):
        self.resume_button = Button(self, "Resume")
        self.quit_button = Button(self, "Quit")
        self.resume_button.set_position(y_pos=(self.height/2))

    def _load_text(self):
        self.text_image = self.font.render(
            "PAUSED", False, self.text_color, self.background_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.midtop = self.rect.midtop
        self.text_image_rect.y += 60

    def check_buttons(self, mouse_pos):
        if self.resume_button.check_button(mouse_pos):
            return 1
        elif self.quit_button.check_button(mouse_pos):
            return 2
        return False

    def update(self):
        self.fill(self.background_color, self.rect)
        self.blit(self.text_image, self.text_image_rect)
        self.quit_button.blitme()
        self.resume_button.blitme()
