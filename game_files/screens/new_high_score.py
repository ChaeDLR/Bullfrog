import pygame.font
from pygame import Surface
from .button import Button
from .menu_base import MenuBase

class NewHighScore(MenuBase):
    """
        When the game ends if the player has reached a new high score
        Show this screen
    """

    def __init__(self, width: int, height: int, stats):
        super(NewHighScore, self).__init__((width, height))

        self._load_button()
        self._load_text(stats.high_score)
    
    def _load_button(self):
        self.play_button = Button(self, "Play")
        self.quit_button = Button(self, "Quit")

        self.play_button.set_position(y_pos=self.rect.height/2)
    
    def set_high_score_img(self, new_high_score: int):
        font = pygame.font.SysFont(None, 50, bold=True)
        self.new_hs_img = font.render(
            f"{new_high_score}", True, self.text_color, self.background_color
        )

    def _load_text(self, new_high_score: int):
        font = pygame.font.SysFont(None, 50, bold=True)
        self.title_img = font.render(
            "New high score!", True, self.text_color, self.background_color
            )
        self.new_hs_img = font.render(
            f"{new_high_score}", True, self.text_color, self.background_color
        )
        self.title_img_rect = self.title_img.get_rect()
        self.new_hs_img_rect = self.new_hs_img.get_rect()
        self.title_img_rect.midtop = self.rect.midtop
        self.new_hs_img_rect.midtop = self.rect.midtop
        self.title_img_rect.y += 40
        self.new_hs_img_rect.y += 80
    
    def check_buttons(self, mouse_pos):
        if self.play_button.check_button(mouse_pos):
            return 1
        elif self.quit_button.check_button(mouse_pos):
            return 2
        return -1
    
    def update(self):
        self.fill(self.background_color, self.rect)
        self.blit(self.title_img, self.title_img_rect)
        self.blit(self.new_hs_img, self.new_hs_img_rect)
        self.play_button.blitme()
        self.quit_button.blitme()
