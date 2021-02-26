import pygame
from ..game_ui import Game_Ui


class LevelBase(pygame.Surface):
    """
        Base level class that will hold
        all of the basic code needed for a level
    """

    def __init__(
        self, width: int, height: int, settings, stats, game_sound
        ):
        super().__init__((width, height))

        self.rect = pygame.Rect(0, 0, width, height)
        self.width, self.height = width, height

        self.settings = settings
        self.game_sound = game_sound
        self.game_stats = stats
        self.game_ui = Game_Ui(self, settings, self.game_stats)

        self.difficulty_tracker = 1
        self.patroller_difficulty = 0
    
    def load_base_custom_events(self):
        self.player_hit = pygame.USEREVENT+5
        self.unpause_game = pygame.USEREVENT+6
    
    def check_keydown_events(self, event):
        """ check for and respond to player input """
        if event.key == pygame.K_ESCAPE:
            self.pause_events()
        elif event.key == pygame.K_UP:
            self.game_sound.player_movement_sound.play()
            self.player.move_forward()
        elif event.key == pygame.K_DOWN:
            self.game_sound.player_movement_sound.play()
            self.player.move_backward()
        elif event.key == pygame.K_LEFT:
            self.player.move_left()
        elif event.key == pygame.K_RIGHT:
            self.player.move_right()

    def check_keyup_events(self, event):
        if event.key == pygame.K_LEFT:
            self.player.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.player.moving_right = False