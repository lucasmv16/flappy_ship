import pygame  # Library for game development in Python
import sys  # System-related functionalities and interactions
import time  # Functions related to time and pauses
import random  # Functions for generating random numbers
import json  # Handling data in JSON format

from pygame.locals import *  # Import constants and events from pygame.locals
from settings.screen import *  # Screen configurations for the game

##screen##
screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption('Flappy Ship')
clock = pygame.time.Clock()

##background##
bif = './assets/images/bg-game.jpg'

bgw = sw
bgh = sh
bg =  pygame.image.load(bif).convert_alpha()
bg = pygame.transform.scale(bg, (bgw,bgh))

##player##
bif = "./assets/images/nave.png"
player_nave = pygame.image.load(bif).convert_alpha()
player_nave = pygame.transform.scale(player_nave, (60,60))
player_nave = pygame.transform.rotate(player_nave, -90)

x_player = sw / 4
y_player = sh / 4
gravity = 0
player_jump = 7.5

min_y_player = 0
max_y_player = sh

##shot##
bif = "./assets/images/fire.png"
missil = pygame.image.load(bif).convert_alpha()
missil = pygame.transform.scale(missil, (30,30))

vel_x_missil = 0
pos_x_missil = -31
pos_y_missil = -31
shot_moven = False
shot_back = True

##obstacle##  
bif = "./assets/images/pilar.png"
obstacle = pygame.image.load(bif).convert_alpha()
new_obstacle = True

obstacles = [700, 1200, 1700, 2200, 2700]
generate_places = True
pos_y_obstacle = []

##score##
score = 0
progress = 0