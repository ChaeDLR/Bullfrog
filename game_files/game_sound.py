import pygame
import os


class GameSound:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        self._load_sound_assets()
        self.music_volume, self.effects_volume = 0.1, 0.3
        # create a whole number to represent the decimals of the volumes
        # Used for creating the number image in settings menu
        self.music_volume_number, self.effects_volume_number = 1, 3
        self.set_music_volume(self.music_volume)
        self.set_effects_volume(self.effects_volume)

    def _load_sound_assets(self):
        """ Load sound from assets folder """
        path = os.path.dirname(__file__)
        self.player_movement_sound = pygame.mixer.Sound(
            os.path.join(path, 'assets/player_movement_sound.wav'))
        self.player_impact_sound = pygame.mixer.Sound(
            os.path.join(path, 'assets/player_impact.wav'))
        pygame.mixer.music.load(os.path.join(
            path, 'assets/background_music.mp3'))

    def set_effects_volume(self, effects_volume: float):
        """
            effects_volume: (0.0 - 1.0)
        """
        self.player_movement_sound.set_volume(effects_volume)
        self.player_impact_sound.set_volume(effects_volume)

    def set_music_volume(self, music_volume: float):
        """
            music_volume: (0.0 - 1.0)
        """
        pygame.mixer.music.set_volume(music_volume)

    def increase_effects_volume(self):
        if self.effects_volume < 1.0:
            self.effects_volume += 0.1
            self.effects_volume = round(self.effects_volume, 2)
            self.effects_volume_number += 1
            self.set_effects_volume(self.effects_volume)

    def decrease_effects_volume(self):
        if self.effects_volume > 0.0:
            self.effects_volume -= 0.1
            self.effects_volume = round(self.effects_volume, 2)
            self.effects_volume_number -= 1
            self.set_effects_volume(self.effects_volume)

    def increase_music_volume(self):
        if self.music_volume < 1.0:
            self.music_volume += 0.1
            self.music_volume = round(self.music_volume, 2)
            self.music_volume_number += 1
            self.set_music_volume(self.music_volume)

    def decrease_music_volume(self):
        if self.music_volume > 0.0:
            self.music_volume -= 0.1
            self.music_volume = round(self.music_volume, 2)
            self.music_volume_number -= 1
            self.set_music_volume(self.music_volume)
