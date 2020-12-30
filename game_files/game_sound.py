import pygame
import os


class GameSound:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        self._load_sound_assets()
        self.set_volume(0.1, 0.3)

    def _load_sound_assets(self):
        """ Load sound from assets folder """
        path = os.path.dirname(__file__)
        self.player_movement_sound = pygame.mixer.Sound(
            os.path.join(path, 'assets/player_movement_sound.wav'))
        self.player_impact_sound = pygame.mixer.Sound(
            os.path.join(path, 'assets/player_impact.wav'))
        pygame.mixer.music.load(os.path.join(
            path, 'assets/background_music.mp3'))

    def set_volume(self, music_volume: float, effects_volume: float):
        """
            Set game volume (music_volumn: (0.0 - 1.0), effects_volume: (0.0, 1.0))
        """
        pygame.mixer.music.set_volume(music_volume)
        self.player_movement_sound.set_volume(effects_volume)
        self.player_impact_sound.set_volume(effects_volume)
