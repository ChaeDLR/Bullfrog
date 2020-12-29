from pygame import Surface, Rect, sprite
import pygame
from ...colors import dark_teal, orange
from ...sprites import Player, Enemy, Gnat, Laser
from ...environment.wall import Wall
from ...game_stats import GameStats
from ...game_sound import GameSound
from ...game_ui import Game_Ui
import time
import sys


class LevelOne(Surface):

    def __init__(self, width: int, height: int, settings, stats):
        """
            Bullfrog level one
        """
        super(LevelOne, self).__init__((width, height))
        self.background_color = dark_teal
        settings.bg_color = self.background_color
        self.rect = Rect(0, 0, width, height)
        self.width, self.height = width, height
        self.settings = settings

        self._load_sprite_groups()
        self._load_environmnet()
        self._load_custom_events()
        self._load_sprites()
        self._load_sound()

        self.game_stats = stats

        self._create_basic_enemies()
        self.game_ui = Game_Ui(self, settings, self.game_stats)
        pygame.time.set_timer(self.gnat_spawn_event, 1500, True)

    def _load_sound(self):
        self.game_sound = GameSound()
        pygame.mixer.music.play()

    def _load_custom_events(self):
        self.gnat_spawn_event = pygame.USEREVENT+1
        self.gnat_despawn_event = pygame.USEREVENT+2
        self.laser_spawn_event = pygame.USEREVENT+3
        self.laser_despawn_event = pygame.USEREVENT+4

    def _check_keydown_events(self, event):
        """ check for and respond to player input """
        if event.key == pygame.K_ESCAPE:
            self._game_over()
        elif event.key == pygame.K_UP:
            self.game_sound.player_movement_sound.play()
            self.player.move_forward()
        elif event.key == pygame.K_DOWN:
            self.game_sound.player_movement_sound.play()
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

    def _check_events(self):
        """ check for events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_stats.game_active:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP and self.game_stats.game_active:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN and not self.game_stats.game_active:
                mouse_pos = pygame.mouse.get_pos()
                self._check_buttons(mouse_pos)
            # spawn a Gnat enemy
            elif event.type == self.gnat_spawn_event and self.game_stats.game_active:
                self._spawn_gnat()
                pygame.time.set_timer(self.gnat_despawn_event, 1000, True)
                pygame.time.set_timer(self.laser_spawn_event, 700, True)
            elif event.type == self.gnat_despawn_event and self.game_stats.game_active:
                self.gnats.empty()
                pygame.time.set_timer(self.gnat_spawn_event, 1500, True)
            # spawn a laser
            elif event.type == self.laser_spawn_event and self.game_stats.game_active:
                laser = Laser(self.gnat_x_y_dir)
                self.lasers.add(laser)

    def _load_environmnet(self):
        """ Load the walls """
        self.walls.add(Wall((self.width/3, 15), (0, 50)))
        self.walls.add(
            Wall((self.width/3, 15), ((self.width-(self.width/3), 50))))

    def _load_sprites(self):
        """ load the sprites needed for the level """
        self.player = Player(self)

    def _load_sprite_groups(self):
        self.patrollers = sprite.Group()
        self.gnats = sprite.Group()
        self.lasers = sprite.Group()
        self.walls = sprite.Group()

    def _empty_sprite_groups(self):
        self.patrollers.empty()
        self.gnats.empty()
        self.lasers.empty()

    def _game_over(self):
        """ Reset the current level """
        self._empty_sprite_groups()
        self.game_stats.reset_stats()
        self.game_stats.game_active = False
        self.game_stats.active_level = 0
        self.game_stats.game_over = True
        pygame.mixer.music.stop()
        pygame.mouse.set_visible(True)

    def _player_hit(self):
        """ respond to the player getting hit """
        self.game_sound.player_impact_sound.play()
        self._empty_sprite_groups()
        self._create_basic_enemies()
        self.player.reset_player()
        self.game_stats.lives_left -= 1
        self._update_ui()
        self.lasers.empty()
        self.gnats.empty()
        if self.game_stats.lives_left == 0:
            self._game_over()
        pygame.time.set_timer(self.gnat_spawn_event, 1500, True)
        time.sleep(0.5)

    def _create_basic_enemies(self):
        for i in range(1, 5):
            basic_enemy = Enemy(self.width, i)
            self.patrollers.add(basic_enemy)

    def _update_enemies(self):
        """ enemy updates """
        self._update_patrollers()
        self._update_lasers()
        self._update_gnats()

    def _update_gnats(self):
        """
            blit gnats to the screen
        """
        for gnat in self.gnats.sprites():
            self.blit(gnat.image, gnat.rect)

    def _spawn_gnat(self):
        """ spawn a gnat """
        gnat = Gnat(
            (self.settings.screen_width, self.settings.screen_height))
        self.gnat_x_y_dir = [gnat.x, gnat.y, gnat.get_direction()]
        self.gnats.add(gnat)

    def _check_collision(self):
        """
            Check for collision between sprites
        """
        if pygame.sprite.spritecollideany(self.player, self.lasers):
            self._player_hit()
        elif pygame.sprite.spritecollideany(self.player, self.patrollers):
            self._player_hit()
        elif pygame.sprite.spritecollideany(self.player, self.walls):
            self._player_hit()

    def _update_lasers(self):
        """
            call update method
            blit to surface
            check for collision with player
        """
        self.lasers.update()
        for laser in self.lasers.sprites():
            self.blit(laser.image, laser.rect)

    def _update_patrollers(self):
        """ 
            call update method on patrollers sprite group
            check edges, blit to surface
            check for collision with player
        """
        self.patrollers.update()
        for enemy in self.patrollers.sprites():
            enemy.check_edges()
            self.blit(enemy.image, enemy.rect)

    def _update_player(self):
        self.player.update_position()
        self.blit(self.player.image, self.player.rect)
        if self.player.check_position():
            self._empty_sprite_groups()
            self.game_stats.level += 1
            self._update_ui()
            self.player.reset_player()
            self._create_basic_enemies()
            pygame.time.set_timer(self.gnat_spawn_event, 1500, True)
            time.sleep(0.2)

    def _update_ui(self):
        self.game_ui.update_level()
        self.game_ui.update_lives()
        self.game_ui.display_ui()

    def _update_environment(self):
        for wall in self.walls.sprites():
            self.blit(wall.image, wall.rect)

    def update(self):

        self.fill(self.background_color)
        self._check_events()
        self._check_collision()
        self._update_environment()
        self._update_enemies()
        self._update_player()
        self._update_ui()
