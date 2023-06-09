import pygame  # Library for game development in Python
import random  # Functions for generating random numbers
import game

from game.json import json_score #saving your score on a json
from settings.screen import *  # Screen configurations for the game
from game.music import sound_effects, sound  # Sound effects and game music
from menus.interface_ingame import GameoverMenu, GameMenu  # Game interfaces, such as the game over menu


def draw_obstalce(player):
        for i in range(len(game.obstacles)):
            y_coord = game.pos_y_obstacle[i]
            top_rect = pygame.draw.rect(game.screen, (0, 0, 255), [game.obstacles[i], 0, 100, y_coord])
            bot_rect = pygame.draw.rect(game.screen, (0, 0, 255), [game.obstacles[i], y_coord + 275, 100, sh - (y_coord + 70)])

            if top_rect.colliderect(player) or bot_rect.colliderect(player):
                pygame.mixer.music.stop()
                sound_effects(sound["dead"])
                GameoverMenu()

def generate_obs():
    if game.generate_places:
        for i in range(len(game.obstacles)):
            game.pos_y_obstacle.append(random.randint(0, sh - 200))
        game.generate_places = False

def new_obs():
    for i in range(len(game.obstacles)):
        game.obstacles[i] -= 3
        if game.obstacles[i] <= game.x_player and game.new_obstacle == True:
            game.score += 10
            game.progress += 1
            game.new_obstacle = False
            json_score()

        if game.obstacles[i] < -100:
            game.obstacles.remove(game.obstacles[i])
            game.pos_y_obstacle.remove(game.pos_y_obstacle[i])
            game.obstacles.append(random.randint(game.obstacles[-1] + 280, game.obstacles[-1] + 320))
            game.pos_y_obstacle.append(random.randint(0, int(game.sh*0.6)))
            game.new_obstacle = True
