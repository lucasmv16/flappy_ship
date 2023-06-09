import pygame  # Library for game development and multimedia applications
import pygame_menu
import os

from settings.screen import sw, sh  # Screen width and height settings


DISPLAY=pygame.display.set_mode((sw, sh))
SIZE=1
WINDOW_SIZE=(sw, sh)
PLAYER="default"
SCORE=10


def retry():
    from game.play import start_game
    start_game()

def quit():
    os.remove('game_data.json')
    pygame_menu.events.EXIT

def back():
    from menus.interface import MainMenu
    os.remove('game_data.json')
    MainMenu()

def apply():
    pass