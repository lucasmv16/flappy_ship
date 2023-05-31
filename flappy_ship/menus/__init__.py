import pygame
DISPLAY=pygame.display.set_mode((800, 600))
SIZE=0.8
WINDOW_SIZE=(800, 600)
PLAYER="default"
SCORE=10


def retry():
    from game.play import game
    game()

def back():
    from menus.main_menu import MainMenu
    MainMenu()

def apply():
    pass