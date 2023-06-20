import pygame
import game

from game.music import sound_effects, sound  # Sound effects and game music
from menus.interface_ingame import GameoverMenu  # Game interfaces, such as the game over menu


def fall():
    ##fall death##
    if game.y_player >= game.max_y_player - 41 and game.gravity > 0:
        pygame.mixer.music.stop()
        sound_effects(sound["dead"])
        GameoverMenu()

def roof():
    if game.y_player <= game.min_y_player and game.gravity < 0:
        game.y_player = game.min_y_player
        game.gravity = 0
