import pygame.font
from pygame import Surface, Rect
from ..colors import dark_teal, orange


class MenuBase(Surface):
    """ Parent class for the game menus """

    def __init__(self, w_h: tuple):
        super().__init__((w_h[0], w_h[1]))
        # Set menu colors
        self.background_color = dark_teal
        self.text_color = orange
        # set menu font and rect
        self.font = pygame.font.SysFont(None, 56, bold=True)
        self.rect = Rect(0, 0, w_h[0], w_h[1])

        self.width, self.height = w_h[0], w_h[1]