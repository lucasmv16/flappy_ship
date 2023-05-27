import sqlite3
import pygame_menu
import pygame, sys, time
from pygame.locals import *
import sys

sys.path.insert(1, './play')

from settings import *
from sprites import BG


### VARS GLOBAL
DISPLAY=pygame.display.set_mode((800, 600))
SIZE=0.8
WINDOW_SIZE=(800, 600)
###

### Vars com Textos ###
TUTORIAL=[f'Tecla Espaço, voce voa, caso caia voce morre']
ABOUT = [f'Flappy Ship é um trabalho em grupo da faculdade',
         f'Programação: Eduardo Silva, Lucas Margalhães, Matheus Sousa',
         f'Sprites & Design: Eduardo Silva, Henrique Freitas']
ABOUT_STORY = [f'Voce foi destidado a ir para uma missão suicida para um bem maior,',
               f'Sua missão é destruir a nave Mãe para isso, você vai entrar nela e',
               f'destruir por dentro, mas não pense que vai ser facil, com forme você',
               f'avança mas você precisa ser rapido. Boa Sorte']

ABOUT_ENDLESS = [f'Endless é um modo Infinito, para você farmar moedas e competir',
                 f'com seus amigos para ver quem fica mais tempo sem morrer']
PLAYER="default"
SCORE=10
###


### Functions ###
def game():
    exec(open("./play/game.py").read())
###

### Start Pygame init
pygame.init()
###

######### MENUS #########

### MENU STORY ###
story_menu = pygame_menu.Menu("Tutorial", WINDOW_SIZE[0] * SIZE , WINDOW_SIZE[1] * SIZE, theme=pygame_menu.themes.THEME_BLUE)
for m in ABOUT_STORY:
    story_menu.add.label(m, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)

story_menu.add.vertical_margin(30)
story_menu.add.button('Play', game)
#for m in TUTORIAL:
#    story_menu.add.label(m, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
story_menu.add.button('Back', pygame_menu.events.BACK)
###

### MENU ENDLESS ###
endless_submenu = pygame_menu.Menu("About Endless", WINDOW_SIZE[0] * SIZE , WINDOW_SIZE[1] * SIZE, theme=pygame_menu.themes.THEME_BLUE)
for m in ABOUT_ENDLESS:
    endless_submenu.add.label(m, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
endless_submenu.add.button('Back', pygame_menu.events.BACK)

endless_menu = pygame_menu.Menu("Endless", WINDOW_SIZE[0] * SIZE , WINDOW_SIZE[1] * SIZE, theme=pygame_menu.themes.THEME_BLUE)
endless_menu.add.button('Play', game)
endless_menu.add.button('About Endless', endless_submenu)
endless_menu.add.button('Back', pygame_menu.events.BACK)

###

### MENU STATS ###
stats_menu = pygame_menu.Menu("Stats", WINDOW_SIZE[0] * SIZE , WINDOW_SIZE[1] * SIZE, theme=pygame_menu.themes.THEME_BLUE)
stats_menu.add.label(PLAYER, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
stats_menu.add.vertical_margin(30)
#stats_menu quantas partidas ja jogou
#stats_menu Maximo de barreiras que passou

stats_menu.add.button('Back', pygame_menu.events.BACK)
###

### SHOP ###
shop_menu = pygame_menu.Menu("Tutorial", WINDOW_SIZE[0] * SIZE , WINDOW_SIZE[1] * SIZE, theme=pygame_menu.themes.THEME_BLUE)
shop_menu.add.button('Back', pygame_menu.events.BACK)
###

### ABOUT ###
#about_theme = pygame_menu.themes.THEME_DEFAULT.copy()
#about_theme.widget_margin = (0, 0)
about_menu = pygame_menu.Menu("About", WINDOW_SIZE[0] * SIZE , WINDOW_SIZE[1] * SIZE, theme=pygame_menu.themes.THEME_BLUE)
for m in ABOUT:
    about_menu.add.label(m, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
about_menu.add.vertical_margin(30)
about_menu.add.button('Back', pygame_menu.events.BACK)
###

#mytheme.background_color = myimage

### MAIN ###
main_menu = pygame_menu.Menu("Flappy Ship", WINDOW_SIZE[0] * SIZE , WINDOW_SIZE[1] * SIZE , theme=pygame_menu.themes.THEME_BLUE)
main_menu.add.button('Story', story_menu)
main_menu.add.button('Endless', endless_menu)
main_menu.add.button('Stats', stats_menu)
main_menu.add.button('Shop', shop_menu)
main_menu.add.button('About', about_menu)
main_menu.add.button('Quit', pygame_menu.events.EXIT)
###

##########################

if __name__ == '__main__':
    main_menu.mainloop((DISPLAY))