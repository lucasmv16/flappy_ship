import game
import pygame
import os

from pygame import mixer
from menus.interface_ingame import GameMenu  # Game interfaces
from game.music import sound_effects, sound  # Sound effects and game music


def player_jump():
    game.gravity = 0
    game.gravity -= game.player_jump

def shooting():
    game.vel_x_missil = 10
    game.shot_moven = True

    if game.shot_back:
        game.pos_x_missil = game.x_player
        game.pos_y_missil = game.y_player
        game.shot_back = False

def pause():
    pygame.mixer.music.pause()
    GameMenu()