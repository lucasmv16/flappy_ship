import game

from pygame.locals import *  # Import constants and events from pygame.locals
from settings.screen import *  # Screen configurations for the game
from game.music import sound_effects, sound  # Sound effects and game music

def reset():
    sound_effects(sound["soundtrank"])

    ##background##
    game.bgw = sw
    game.bgh = sh
    game.vel = 6
    game.x_heart = sw

    ##player##
    game.x_player = sw / 4
    game.y_player = sh / 4
    game.gravity = 0
    game.player_jump = 7.5

    game.min_y_player = 0
    game.max_y_player = sh

    ##shot##
    game.vel_x_missil = 0
    game.pos_x_missil = -61
    game.pos_y_missil = -61
    game.shot_moven = False
    game.shot_back = True

    ##obstacle##  
    game.new_obstacle = True

    game.obstacles = [700, 1200, 1700, 2200, 2700]
    game.generate_places = True
    game.pos_y_obstacle = []
    game.stop_create = False

    game.des_obstacles = []
    game.y_des_obstacles = []


    ##score##
    game.score = 0
    game.progress = 0

    ##endless##
    game.speed_end = 10