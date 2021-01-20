import pygame.font
import os
from pygame import Surface
from .button import Button
from ..colors import dark_teal, orange


class SettingsMenu(Surface):
    """
        Settings menu
        Allow user to adjust sound volume
    """

    def __init__(self, width: int, height: int, game_sound):
        super(SettingsMenu, self).__init__((width, height))
        self.background_color = dark_teal
        self.text_color = orange
        self.rect = pygame.Rect(0, 0, width, height)

        self.screen_rows = height/6
        self.screen_columns = width/6

        self.width, self.height = width, height

        self.game_sound = game_sound

        self.plus_pressed, self.minus_pressed = False, False

        self._load_images()
        self._load_title()
        self._load_options_text()
        self._load_buttons()

    def update_music_volume_string(self):
        music_volume_string = f'Music volume: {self.game_sound.music_volume_number}'
        font = pygame.font.SysFont(None, 38)
        self.music_volume_image = font.render(
            music_volume_string, True, self.text_color, self.background_color
        )

    def _load_buttons(self):
        """
            Create apply and back buttons
        """
        self.back_button = Button(self, "Back")
        self.back_button.set_position(self.screen_columns, self.screen_rows*5)

    def _load_options_text(self):
        """
            Create available options text
            Set position
        """
        self.update_music_volume_string()
        self.music_volume_image_rect = self.music_volume_image.get_rect()
        self.music_volume_image_rect.y = self.plus_image_rect.bottom
        self.music_volume_image_rect.x = self.screen_rows*2

    def _load_images(self):
        """
            load minus.png and plus.png
            from assets folder and set positions
        """
        path = os.path.dirname(__file__)
        self.plus_image = pygame.image.load(
            os.path.join(path, 'menu_assets/plus.png'))
        self.plus_filled_image = pygame.image.load(
            os.path.join(path, 'menu_assets/plus_filled.png'))
        self.minus_image = pygame.image.load(
            os.path.join(path, 'menu_assets/minus.png'))
        self.minus_filled_image = pygame.image.load(
            os.path.join(path, 'menu_assets/minus_filled.png'))

        self.plus_image_rect = self.plus_image.get_rect()
        self.minus_image_rect = self.minus_image.get_rect()

        self.plus_image_rect.bottom = (self.screen_rows*3)-8
        self.minus_image_rect.top = (self.screen_rows*3)+8

        self.plus_image_rect.x = self.screen_columns*3.2
        self.minus_image_rect.x = self.screen_columns*3.2

    def _load_title(self):
        """ load settings title """
        font = pygame.font.SysFont(None, 56, bold=True)
        self.settings_menu_img = font.render(
            "SETTINGS", True, self.text_color, self.background_color
        )
        self.settings_menu_img_rect = self.settings_menu_img.get_rect()
        self.settings_menu_img_rect.midtop = self.rect.midtop
        self.settings_menu_img_rect.y += 60

    def check_buttons(self, mouse_pos):
        """
            return 1 if plus sign is pressed
            return 2 if minus is pressed
        """
        if self.plus_image_rect.collidepoint(mouse_pos):
            return 1
        elif self.minus_image_rect.collidepoint(mouse_pos):
            return 2
        elif self.back_button.check_button(mouse_pos):
            return 3
        return -1

    def _update_signs(self):
        """
            Update plus and minus signs
        """
        if self.plus_pressed:
            self.blit(self.plus_image, self.plus_image_rect)
            self.plus_pressed = False
        else:
            self.blit(self.plus_filled_image, self.plus_image_rect)

        if self.minus_pressed:
            self.blit(self.minus_image, self.minus_image_rect)
            self.minus_pressed = False
        else:
            self.blit(self.minus_filled_image, self.minus_image_rect)

    def update(self):
        self.fill(self.background_color, self.rect)
        self.blit(self.settings_menu_img, self.settings_menu_img_rect)
        self._update_signs()
        self.blit(self.music_volume_image, self.music_volume_image_rect)
        self.back_button.blitme()
