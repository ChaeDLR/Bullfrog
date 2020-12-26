import pygame.font
from pygame import Surface
from .button import Button


class MainMenu(Surface):

    def __init__(self, width: int, height: int):
        super(MainMenu, self).__init__((width, height))
        self.background_color = (45, 250, 20)
        self.text_color = (255, 55, 55)
        self.font = pygame.font.SysFont(None, 50, bold=True)
        self.rect = pygame.Rect(0, 0, width, height)

        self.width, self.height = width, height

        self._load_title()
        self._load_buttons()

    def _load_buttons(self):
        self.play_button = Button(self, "Play")
        self.quit_button = Button(self, "Quit")

        self.play_button.set_position(y_pos=self.rect.height/2)

    def check_buttons(self, mouse_pos):
        if self.play_button.check_button(mouse_pos):
            return 1
        elif self.quit_button.check_button(mouse_pos):
            return 2
        return -1

    def _load_title(self):
        """ load game title """
        self.main_menu_img = self.font.render(
            "BULLFROG", True, self.text_color, self.background_color)
        self.main_menu_img_rect = self.main_menu_img.get_rect()
        self.main_menu_img_rect.midtop = self.rect.midtop
        self.main_menu_img_rect.y += 40

    def draw_main_menu(self):
        self.fill(self.background_color, self.rect)
        self.blit(self.main_menu_img, self.main_menu_img_rect)
        self.blit(self.play_button, self.play_button.rect)
        self.blit(self.play_button.msg_image, self.play_button.msg_image_rect)
        self.blit(self.quit_button, self.quit_button.rect)
        self.blit(self.quit_button.msg_image, self.quit_button.msg_image_rect)