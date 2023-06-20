import pygame  # Library for game development in Python
import random  # Functions for generating random numbers
import game

from game.shot import death_shot
from game.json import json_score #saving your score on a json
from settings.screen import *  # Screen configurations for the game
from game.music import sound_effects, sound  # Sound effects and game music
from menus.interface_ingame import GameoverMenu, GameoverEndMenu  # Game interfaces, such as the game over menu


def draw_obstalce(player, shot):
        for i in range(len(game.obstacles)):
            y_coord = game.pos_y_obstacle[i]
            top_rect = pygame.draw.rect(game.screen, (150, 150, 150), [game.obstacles[i], 0, 100, y_coord])
            bot_rect = pygame.draw.rect(game.screen, (150, 150, 150), [game.obstacles[i], y_coord + 275, 100, sh - (y_coord + 70)])


            if top_rect.colliderect(player) or bot_rect.colliderect(player):
                pygame.mixer.music.stop()
                sound_effects(sound["dead"])
                if game.endless:
                    GameoverEndMenu()
                else:
                    GameoverMenu()
            if top_rect.colliderect(shot) or bot_rect.colliderect(shot):
                death_shot()
        for d in range (len(game.des_obstacles)):
            try:
                y_coord = game.y_des_obstacles[d]
                destroy = pygame.draw.rect(game.screen, (100, 100, 100), [game.des_obstacles[d], y_coord, 100, 275])
                if destroy.colliderect(shot):
                    death_shot()
                    game.des_obstacles.remove(game.des_obstacles[d])
                    game.y_des_obstacles.remove(game.y_des_obstacles[d])
                    game.score += 5
                if destroy.colliderect(player):
                    pygame.mixer.music.stop()
                    sound_effects(sound["dead"])
                    if game.endless:
                        GameoverEndMenu()
                    else:
                        GameoverMenu()
            except:
                pass
            

def generate_obs():
    if game.generate_places:
        for i in range(len(game.obstacles)):
            game.pos_y_obstacle.append(random.randint(0, sh - 200))
        game.generate_places = False

def new_obs():
    for i in range(len(game.obstacles)):
        if not game.obstacles[i] <= -102 - game.vel:
            game.obstacles[i] -= game.vel
        if game.obstacles[i] <= game.x_player and game.new_obstacle == True:
            game.score += 10
            game.progress += 1
            game.new_obstacle = False
            json_score()

        if game.obstacles[i] < -100 and game.obstacles[i] > -101 -game.vel:
            if not game.stop_create:
                game.obstacles.remove(game.obstacles[i])
                game.pos_y_obstacle.remove(game.pos_y_obstacle[i])
                game.obstacles.append(random.randint(game.obstacles[-1] + 400, game.obstacles[-1] + 500))
                game.pos_y_obstacle.append(random.randint(0, int(game.sh*0.6)))

                if random.randint(1, 10) >= 9:
                    game.des_obstacles.append(game.obstacles[-1])
                    game.y_des_obstacles.append(game.pos_y_obstacle[-1])
            game.new_obstacle = True

    for i in range(len(game.des_obstacles)):
        if not game.des_obstacles[i] <= -102 - game.vel:
            game.des_obstacles[i] -= game.vel