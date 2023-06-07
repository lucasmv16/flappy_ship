import pygame  # Library for game development and multimedia applications

from settings.screen import sw, sh  # Screen width and height settings


DISPLAY=pygame.display.set_mode(((sw/1.5), (sh/1.5)), pygame.RESIZABLE)
SIZE=1
WINDOW_SIZE=(sw/1.5, sh/1.5)
PLAYER="default"
SCORE=10


def retry():
    from game.play import game
    game()

def back():
    from menus.interface import MainMenu
    MainMenu()

def apply():
    pass