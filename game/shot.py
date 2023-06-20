import game
import pygame

from menus.interface_ingame import VictoryMenu

def shot_move():
    if game.shot_moven == True:
            game.pos_x_missil += game.vel_x_missil #fazendo o tiro ter o movimento

def death_shot():
    game.pos_x_missil = -31
    game.pos_y_missil = -31
    game.shot_back = True
    game.shot_moven = False

def shot_collision(shot, heart):
     if shot.colliderect(heart) and game.vel == 0:
        death_shot()
        pygame.mixer.music.stop()
        VictoryMenu()