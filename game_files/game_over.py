import pygame.font


class Game_Over:

    def __init__(self, bullfrog):
        self.screen = bullfrog.screen
        self.screen_rect = self.screen.get_rect()

        self.background_color = bullfrog.settings.bg_color

        self.text_color = (255, 50, 50)

        self.font = pygame.font.SysFont(None, 50, bold=True)

        self.rect = pygame.Rect(0, 0, 200, 50)
        self.rect.x, self.rect.y = bullfrog.settings.screen_width / \
            2-100, bullfrog.settings.screen_height/6

        self.game_over_img = self.font.render(
            "Game Over", True, self.text_color, bullfrog.settings.bg_color)
        self.game_over_img_rect = self.game_over_img.get_rect()
        self.game_over_img_rect.center = self.rect.center

    def draw_game_over(self):

        self.screen.fill(self.background_color, self.rect)
        self.screen.blit(self.game_over_img, self.game_over_img_rect)
