# Chae DeLaRosa
import pygame
import sys
import random
import time
import game_files


class BullFrog:
    """ Main game """

    def __init__(self):
        """ initialize game screens, clock, settings, and stats """
        pygame.init()
        self.settings = game_files.Settings()
        # create screen
        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        # set caption
        pygame.display.set_caption("Bullfrog")
        # pygame clock
        self.clock = pygame.time.Clock()

        self.stats = game_files.GameStats()

        self._load_game_screens()

    def _load_game_screens(self):
        """ Load start and game over screens """
        self.main_menu = game_files.MainMenu(
            self.settings.screen_width, self.settings.screen_height)
        self.game_over = game_files.Game_Over(
            self.settings.screen_width, self.settings.screen_height)

    def run_game(self):
        """ main loop """
        while True:
            self.clock.tick(60)
            if self.stats.game_active == False:
                self._check_events()
            self._update_screen()

    def _check_events(self):
        """ check for events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not self.stats.game_active:
                mouse_pos = pygame.mouse.get_pos()
                self._check_buttons(mouse_pos)

    def _check_keydown_events(self, event):
        """ check for and respond to player input """
        if event.key == pygame.K_q:
            sys.exit()

    def _start_game(self):
        """ Reset the game """
        self.level_one = game_files.LevelOne(
            self.settings.screen_width, self.settings.screen_height, self.settings, self.stats)
        # reset game
        self.stats.game_active = True
        self.stats.game_over = False
        self.stats.active_level = 1
        pygame.mouse.set_visible(False)

    def _check_buttons(self, mouse_pos):
        """
            check of buttons on the game over screen or main menu are being pressed
        """
        if self.game_over.check_buttons(mouse_pos) == 1 and self.stats.game_over:
            self._start_game()
        elif self.game_over.check_buttons(mouse_pos) == 2 and self.stats.game_over:
            sys.exit()

        if self.main_menu.check_buttons(mouse_pos) == 1:
            self._start_game()
        elif self.main_menu.check_buttons(mouse_pos) == 2:
            sys.exit()

    def _stop_game(self):
        """Game Over"""
        self.stats.game_active = False
        self.stats.game_over = True
        pygame.mouse.set_visible(True)

    def _show_gameover_screen(self):
        """ display the game over screen """
        self.game_over.update_screen()
        self.screen.blit(self.game_over, (0, 0))

    def _show_main_menu(self):
        """ display the main menu screen """
        self.main_menu.draw_main_menu()
        self.screen.blit(self.main_menu, (0, 0))

    def _show_level_one(self):
        self.level_one.update()
        self.screen.blit(self.level_one, self.level_one.rect)

    def _update_screen(self):
        """ things to be updated """
        self.screen.fill(self.settings.bg_color)

        if self.stats.active_level == 1 and self.stats.game_active:
            self._show_level_one()
        elif self.stats.lives_left == 0:
            self._stop_game()

        elif not self.stats.game_active and self.stats.game_over == True:
            self._show_gameover_screen()

        elif not self.stats.game_active:
            self._show_main_menu()

        pygame.display.flip()


if __name__ == '__main__':
    theBullFrog = BullFrog()
    theBullFrog.run_game()
