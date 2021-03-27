from pygame import sprite
import pygame
from ..colors import dark_teal, orange, olive_green
from ..sprites import Enemy, Gnat, Laser, PatrollerGnat
from ..environment.wall import Wall
from .level_base import LevelBase
import time
import sys


class LevelTwo(LevelBase):

    def __init__(
        self, width: int, height: int, settings: object, stats: object, game_sound: object
        ):
        """
            Bullfrog level two
        """
        super().__init__(width, height, settings, stats, game_sound)
        self.background_color = olive_green
        settings.bg_color = self.background_color
        
        self.enemy_count = 7
        self.difficulty_tracker = 1
        self.patroller_difficulty = 0

        self._load_sprite_groups()
        self._load_environmnet()
        self._load_custom_events()

        self._create_basic_enemies()

        pygame.time.set_timer(self.gnat_spawn_event, 1500)
        pygame.time.set_timer(self.pat_gnat_laser_event, 2000)

    def _load_custom_events(self):
        self.gnat_spawn_event = pygame.USEREVENT+1
        self.gnat_despawn_event = pygame.USEREVENT+2
        self.laser_spawn_event = pygame.USEREVENT+3
        self.laser_despawn_event = pygame.USEREVENT+4
        self.pat_gnat_laser_event = pygame.USEREVENT+7
        self.load_base_custom_events()

    def _check_events(self):
        """ Levels main check events loop """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_stats.game_active:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP and self.game_stats.game_active:
                self.check_keyup_events(event)
            else:
                self._check_custom_events(event)

    def _check_custom_events(self, event):
        # spawn a Gnat enemy
        if event.type == self.player_hit and self.game_stats.game_active:
            self._player_hit()
        elif event.type == self.gnat_spawn_event and self.game_stats.game_active:
            self._spawn_gnat()
            pygame.time.set_timer(self.laser_spawn_event, 250, True)
        elif event.type == self.laser_spawn_event and self.game_stats.game_active and self.gnats.sprites():
            laser = Laser(self.gnat_x_y_dir)
            self.lasers.add(laser)
        elif event.type == self.pat_gnat_laser_event and self.game_stats.game_active:

            pos_dir_list = [self.patroller_gnats.sprites()[0].rect.x,
                            self.patroller_gnats.sprites()[0].rect.y, 1]
            laser = Laser(pos_dir_list, 1)
            self.pat_gnat_lasers.add(laser)
        elif event.type == self.unpause_game:
            pygame.mixer.music.unpause()

    def _load_environmnet(self):
        """ Load the walls """
        self.walls.add(Wall((self.width/3, 15), (0, 50)))
        self.walls.add(
            Wall((self.width/3, 15), ((self.width-(self.width/3), 50))))

    def _load_sprite_groups(self):
        self.patrollers = sprite.Group()
        self.gnats = sprite.Group()
        self.lasers = sprite.Group()
        self.walls = sprite.Group()
        self.patroller_gnats = sprite.Group()
        self.pat_gnat_lasers = sprite.Group()

    def _empty_sprite_groups(self):
        self.patrollers.empty()
        self.gnats.empty()
        self.lasers.empty()
        self.patroller_gnats.empty()
        self.pat_gnat_lasers.empty()

    def _game_over(self):
        """ Reset the current level """
        self.base_game_over()
        self._empty_sprite_groups()

    def _player_hit(self):
        """ respond to the player getting hit """
        self._empty_sprite_groups()
        self._create_basic_enemies()
        self.player.reset_player()
        self.player.player_hit = False
        self.game_stats.lives_left -= 1
        self.update_ui()
        if self.game_stats.lives_left == 0:
            self._game_over()

    def _create_basic_enemies(self):
        for i in range(2, self.enemy_count):
            basic_enemy = Enemy((self.width, self.height), i)
            basic_enemy.set_enemy_speed(self.patroller_difficulty)
            self.patrollers.add(basic_enemy)
        patroller_gnat = PatrollerGnat((self.width, self.height))
        self.patroller_gnats.add(patroller_gnat)

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
            if not gnat.check_life_length():
                self.gnats.remove(gnat)
            self.blit(gnat.image, gnat.rect)

    def _spawn_gnat(self):
        """ spawn a gnat """
        gnat = Gnat(
            (self.settings.screen_width, self.settings.screen_height), 1)
        self.gnat_x_y_dir = [gnat.x, gnat.y, gnat.get_direction()]
        self.gnats.add(gnat)

    def _player_collide_hit(self):
        """
            If the player collides with something that hurts it
        """
        if self.player.player_hit == False:
            self.game_sound.player_impact_sound.play()
        self.player.player_hit = True
        pygame.time.set_timer(self.player_hit, 500, True)

    def _check_collision(self):
        """
            Check for collision between sprites
        """
        if pygame.sprite.spritecollideany(self.player, self.lasers):
            self.player_collide_hit()
        if pygame.sprite.spritecollideany(self.player, self.patrollers):
            self.player_collide_hit()
        if pygame.sprite.spritecollideany(self.player, self.walls):
            self.player_collide_hit()
        if pygame.sprite.spritecollideany(self.player, self.gnats):
            self.player_collide_hit()
        if pygame.sprite.spritecollideany(self.player, self.patroller_gnats):
            self.player_collide_hit()
        if pygame.sprite.spritecollideany(self.player, self.pat_gnat_lasers):
            self.player_collide_hit()
        for patroller in self.patrollers:
            if pygame.sprite.spritecollideany(patroller, self.walls):
                patroller.change_direction()

    def _update_lasers(self):
        """
            call update method
            blit to surface
            check for collision with player
        """
        for laser in self.lasers.sprites():
            laser.update_horizontal()
            self.blit(laser.image, laser.rect)

        for las in self.pat_gnat_lasers.sprites():
            las.update_vert()
            self.blit(las.image, las.rect)

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
        self.patroller_gnats.update()
        for pat_gnat in self.patroller_gnats.sprites():
            self.blit(pat_gnat.image, pat_gnat.rect)

    def _next_level(self):
        self._empty_sprite_groups()
        self.game_stats.level += 1
        self.difficulty_tracker += 1
        self.update_ui()
        self.player.reset_player()
        self._create_basic_enemies()
        if self.difficulty_tracker == 5:
            self.difficulty_tracker = 1
            if self.patroller_difficulty < 3:
                self.patroller_difficulty += 1

    def _show_player_hit(self):
        if self.player.death_frame % 2 == 0:
            self.blit(self.player.player_hit_images[0], self.player.rect)
        else:
            self.blit(self.player.player_hit_images[1], self.player.rect)
        self.player.death_frame += 1
        time.sleep(0.1)

    def _update_player(self):
        if self.player.player_hit:
            self._show_player_hit()
        else:
            self.blit(self.player.image, self.player.rect)

        if self.player.check_position():
            self._next_level()

    def _update_environment(self):
        for wall in self.walls.sprites():
            self.blit(wall.image, wall.rect)

    def update(self):
        self.fill(self.background_color)
        self._check_collision()
        self._update_environment()
        self._update_enemies()
        self._update_player()
        self.update_ui()
        self._check_events()
