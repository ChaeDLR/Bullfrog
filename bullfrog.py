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
        # enemy group
        self.enemys = pygame.sprite.Group()
        # pygame clock
        self.clock = pygame.time.Clock()
        # create enemys
        self._create_enemys()
        # create the player
        self.player = game_files.Player(self)
        # create play button
        self.play_button = game_files.Button(self)
        # create scoreboard
        self.sb = game_files.Scoreboard(self)

        self.gs = game_files.GameSound()

        self.game_over_flag = False

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # returns mouse x,y cords
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """ respond if the play button has been pressed """
        # check if the mouse clicked the button
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.stats.game_active:
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
        self.player.blitme()
        if self.player.check_position():
            self.enemys.empty()
            self.stats.level += 1
            self.settings.change_bg_color()
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
        time.sleep(0.5)

    def _create_enemys(self):
        """ create enemys """
        for row_number in range(1, 5):
            self._create_enemy(row_number)

    def _create_enemy(self, row_number):
        """ create enemy """
        enemy = game_files.Enemy(self)
        enemy.enemy_speed = random.randint(3, 8)
        enemy.enemy_direction = random.choice((-1, 1))
        enemy.y = row_number * 100
        enemy.x = enemy.enemy_direction * enemy.enemy_speed + 300
        enemy.rect.x = enemy.x
        enemy.rect.y = enemy.y
        self.enemys.add(enemy)

    def _update_enemy(self):
        """ enemy updates """
        self.enemys.update()
        for enemy in self.enemys.sprites():
            enemy.check_edges()
        if pygame.sprite.spritecollideany(self.player, self.enemys):
            self._player_hit()

    def game_over(self):
        """Game Over"""
        self.stats.game_active = False
        self.game_over_flag = True
        pygame.mouse.set_visible(True)
        pygame.mixer.music.stop()
        self.stats.reset_stats()
        self.settings.reset_background()
        self.sb.prep_lives()
        self.sb.prep_level()

    def _update_screen(self):
        """ things to be updated """
        # set the window background color
        self.screen.fill(self.settings.bg_color)
        # draw enemys
        self.enemys.draw(self.screen)
        # display player
        self._update_player()
        # display scoreboard
        self.sb.show_score()

        if self.stats.lives_left == 0:
            self.game_over()

        if not self.stats.game_active and self.game_over_flag == True:
            game_over_text = game_files.Game_Over(self)
            game_over_text.draw_game_over()
            self.play_button.draw_button()
        elif not self.stats.game_active:
            self.play_button.draw_button()
        # draw a new screen
        pygame.display.flip()


if __name__ == '__main__':
    theBullFrog = BullFrog()
    theBullFrog.run_game()
