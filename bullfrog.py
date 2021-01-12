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
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Bullfrog")
        self.clock = pygame.time.Clock()
        self.stats = game_files.GameStats()
        self.game_sound = game_files.GameSound()

        self._load_game_screens()

    def _load_game_screens(self):
        """ Load start and game over screens """
        self.main_menu = game_files.MainMenu(
            self.settings.screen_width, self.settings.screen_height
        )
        self.game_over = game_files.Game_Over(
            self.settings.screen_width, self.settings.screen_height
        )
        self.pause_menu = game_files.PauseMenu(
            self.settings.screen_width, self.settings.screen_height
        )
        self.settings_menu = game_files.SettingsMenu(
            self.settings.screen_width, self.settings.screen_height,
            self.game_sound
        )
        self._load_level_one()
    
    def _load_level_one(self):
        self.level_one = game_files.LevelOne(
            self.settings.screen_width, self.settings.screen_height, 
            self.settings, self.stats, self.game_sound
        )

    def run_game(self):
        """ main loop """
        while True:
            self.clock.tick(60)

            if self.stats.game_paused:
                self._check_paused_events()
            elif self.stats.game_active == False:
                self._check_events()

            self._update_screen()

    def _check_paused_events(self):
        """
            Check for events on the pause screen
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_pause_menu_buttons(mouse_pos)

    def _check_events(self):
        """ check for events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not self.stats.game_active:
                mouse_pos = pygame.mouse.get_pos()

                if self.stats.game_over:
                    self._check_game_over_buttons(mouse_pos)
                
                elif self.stats.settings_menu_active:
                    self._check_settings_menu_buttons(mouse_pos)
                
                elif self.stats.main_menu_active:
                    self._check_main_menu_buttons(mouse_pos)

    def _check_keydown_events(self, event):
        """ check for and respond to player input """
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def _start_game(self):
        """ Reset the game """
        # reset game
        self._load_level_one()
        self.stats.main_menu_active = False
        self.stats.game_active = True
        self.stats.game_over = False
        self.stats.active_level = 1
        pygame.mouse.set_visible(False)
        pygame.mixer.music.play()

    def _unpause_game(self):
        self.stats.game_active = True
        self.stats.game_paused = False
        self.level_one.resume_game()
        pygame.mouse.set_visible(False)

    def _check_pause_menu_buttons(self, mouse_pos):
        """
            self.stats.game_paused
        """
        if self.pause_menu.check_buttons(mouse_pos) == 1:
            self._unpause_game()
        elif self.pause_menu.check_buttons(mouse_pos) == 2:
            sys.exit()
    
    def _check_game_over_buttons(self, mouse_pos):
        """
            self.stats.game_over
        """
        if self.game_over.check_buttons(mouse_pos) == 1:
            self._start_game()
        elif self.game_over.check_buttons(mouse_pos) == 2:
            sys.exit()
    
    def _check_settings_menu_buttons(self, mouse_pos):
        """
            self.stats.settings_menu_active
        """
        if self.settings_menu.check_buttons(mouse_pos) == 1:
            self.game_sound.increase_music_volume()
            self.settings_menu.update_music_volume_string()
        elif self.settings_menu.check_buttons(mouse_pos) == 2:
            self.game_sound.decrease_music_volume()
            self.settings_menu.update_music_volume_string()
        elif self.settings_menu.check_buttons(mouse_pos) == 3:
            self.stats.set_active_screen(main_menu=True)

    def _check_main_menu_buttons(self, mouse_pos):
        """
            self.stats.main_menu_active
        """
        if self.main_menu.check_buttons(mouse_pos) == 1:
            self._start_game()
        elif self.main_menu.check_buttons(mouse_pos) == 2:
            sys.exit()
        elif self.main_menu.check_buttons(mouse_pos) == 3:
            self.stats.set_active_screen(settings_menu=True)

    def _stop_game(self):
        """Game Over"""
        self.stats.game_active = False
        self.stats.game_over = True
        pygame.mouse.set_visible(True)

    def _active_screen(self):

        if self.stats.lives_left == 0:
            self._stop_game()
        elif self.stats.active_level == 1 and self.stats.game_active:
            return self.level_one

        elif not self.stats.game_active and self.stats.game_over:
            return self.game_over

        elif not self.stats.game_active and self.stats.game_paused:
            return self.pause_menu

        elif not self.stats.game_active and self.stats.settings_menu_active:
            return self.settings_menu

        elif not self.stats.game_active and self.stats.main_menu_active:
            return self.main_menu

    def _update_screen(self):
        """ things to be updated """
        if not self.stats.game_paused:
            self.screen.fill(self.settings.bg_color)
            active_screen = self._active_screen()
            active_screen.update()
            self.screen.blit(active_screen, active_screen.rect)
        else:
            self.pause_menu.update()
            self.screen.blit(self.pause_menu, self.pause_menu.rect)
        pygame.display.flip()

if __name__ == '__main__':
    theBullFrog = BullFrog()
    theBullFrog.run_game()
