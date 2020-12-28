# Chae DeLaRosa
import pygame
import sys
import random
import time
import game_files


class BullFrog:
    """ Main game """

    def __init__(self):
        """ initialize our game variables """

        # intialize pygame
        pygame.init()
        self.settings = game_files.Settings()
        self.stats = game_files.GameStats(self)
        # create screen
        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        # set caption
        pygame.display.set_caption("Bullfrog")
        self._load_sprite_groups()
        self._load_custom_events()
        # pygame clock
        self.clock = pygame.time.Clock()
        # create enemys
        self._create_enemys()
        # create the player
        self.player = game_files.Player(self)
        # create scoreboard
        self.sb = game_files.Scoreboard(self)

        self.gs = game_files.GameSound()

        self._load_game_screens()

        self.game_over_flag = False

    def _load_sprite_groups(self):
        self.enemys = pygame.sprite.Group()
        self.gnats = pygame.sprite.Group()
        self.lasers = pygame.sprite.Group()

    def _load_custom_events(self):
        self.gnat_spawn_event = pygame.USEREVENT+1
        self.gnat_despawn_event = pygame.USEREVENT+2
        self.laser_spawn_event = pygame.USEREVENT+3
        self.laser_despawn_event = pygame.USEREVENT+4

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
            self._check_events()
            if self.stats.game_active:
                self._update_enemy()
            # update the screen
            self._update_screen()

    def _check_events(self):
        """ check for events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.stats.game_active:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP and self.stats.game_active:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN and not self.stats.game_active:
                mouse_pos = pygame.mouse.get_pos()
                self._check_buttons(mouse_pos)
            # spawn a Gnat enemy
            elif event.type == self.gnat_spawn_event and self.stats.game_active:
                self._spawn_gnat()
                pygame.time.set_timer(self.gnat_despawn_event, 1000, True)
                pygame.time.set_timer(self.laser_spawn_event, 700, True)
            elif event.type == self.gnat_despawn_event and self.stats.game_active:
                self.gnats.empty()
                pygame.time.set_timer(self.gnat_spawn_event, 1500, True)
            # spawn a laser
            elif event.type == self.laser_spawn_event and self.stats.game_active:
                laser = game_files.Laser(self.gnat_x_y_dir)
                self.lasers.add(laser)

    def _reset_game(self):
        """ Reset the game """
        # reset game
        self.stats.reset_stats()
        self.stats.game_active = True
        self.game_over_flag = False
        self.enemys.empty()
        pygame.mouse.set_visible(False)
        self._create_enemys()
        self.player.reset_player()
        pygame.mixer.music.play()
        self.sb.prep_level()
        pygame.time.set_timer(self.gnat_spawn_event, 2000)

    def _check_buttons(self, mouse_pos):
        """ respond if the play button has been pressed """
        if self.game_over.check_buttons(mouse_pos) == 1 and self.game_over_flag:
            self._reset_game()
        elif self.game_over.check_buttons(mouse_pos) == 2 and self.game_over_flag:
            sys.exit()

        if self.main_menu.check_buttons(mouse_pos) == 1:
            self._reset_game()
        elif self.main_menu.check_buttons(mouse_pos) == 2:
            sys.exit()

    def _check_keydown_events(self, event):
        """ check for and respond to player input """
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.gs.player_movement_sound.play()
            self.player.move_forward()
        elif event.key == pygame.K_DOWN:
            self.gs.player_movement_sound.play()
            self.player.move_backward()
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.player.moving_right = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_LEFT:
            self.player.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.player.moving_right = False

    def _update_player(self):
        """ player values that need to be updated """
        self.player.update_position()
        self.screen.blit(self.player.image, self.player.rect)
        if self.player.check_position():
            self.enemys.empty()
            self.gnats.empty()
            self.lasers.empty()
            self.stats.level += 1
            self.sb.prep_level()
            self.player.reset_player()
            self._create_enemys()
            time.sleep(0.2)

    def _player_hit(self):
        """ respond to the player getting hit """
        self.gs.player_impact_sound.play()
        self.enemys.empty()
        self._create_enemys()
        self.player.reset_player()
        self.stats.lives_left -= 1
        self.sb.prep_lives()
        self.sb.prep_level()
        self.lasers.empty()
        self.gnats.empty()
        time.sleep(0.5)

    def _spawn_gnat(self):
        """ spawn a gnat """
        gnat = game_files.Gnat(
            (self.settings.screen_width, self.settings.screen_height))
        self.gnat_x_y_dir = [gnat.x, gnat.y, gnat.get_direction()]
        self.gnats.add(gnat)

    def _create_enemys(self):
        """ create enemys """
        for row_number in range(1, 5):
            enemy = game_files.Enemy(self.settings.screen_width, row_number)
            self.enemys.add(enemy)

    def _update_enemy(self):
        """ enemy updates """
        self.enemys.update()
        self.lasers.update()
        for enemy in self.enemys.sprites():
            enemy.check_edges()
        if pygame.sprite.spritecollideany(self.player, self.enemys):
            self._player_hit()
        elif pygame.sprite.spritecollideany(self.player, self.lasers):
            self._player_hit()

    def _stop_game(self):
        """Game Over"""
        self.stats.game_active = False
        self.game_over_flag = True
        pygame.mouse.set_visible(True)
        pygame.mixer.music.stop()
        self.stats.reset_stats()
        self.sb.prep_lives()
        self.sb.prep_level()

    def _show_gameover_screen(self):
        """ display the game over screen """
        self.game_over.update_screen()
        self.screen.blit(self.game_over, (0, 0))

    def _show_main_menu(self):
        """ display the main menu screen """
        self.main_menu.draw_main_menu()
        self.screen.blit(self.main_menu, (0, 0))

    def _update_screen(self):
        """ things to be updated """
        self.screen.fill(self.settings.bg_color)
        self.enemys.draw(self.screen)
        self.gnats.draw(self.screen)
        self.lasers.draw(self.screen)
        self._update_player()
        self.sb.show_score()

        if self.stats.lives_left == 0:
            self._stop_game()

        if not self.stats.game_active and self.game_over_flag == True:
            self._show_gameover_screen()
        elif not self.stats.game_active:
            self._show_main_menu()

        pygame.display.flip()


if __name__ == '__main__':
    theBullFrog = BullFrog()
    theBullFrog.run_game()
