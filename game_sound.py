import pygame
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()


player_movement_sound = pygame.mixer.Sound('assets/player_movement_sound.wav')
player_impact_sound = pygame.mixer.Sound('assets/player_impact.wav')
pygame.mixer.music.load('assets/background_music.mp3')
pygame.mixer.music.set_volume(0.1)