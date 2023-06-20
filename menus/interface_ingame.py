import pygame  # Library for game development and multimedia applications
import pygame_menu  # Library for creating menus in pygame
import json  # Library for working with JSON data
import menus  # Custom module for game menus
import os

from settings.screen import *
from game.json import perm_json # saving the high score
from menus.theme import theme  # Custom theme module for menu styling
from menus.theme import font  # Custom module for defining fonts in the menu


### VARS GLOBAL ###


### GAMEOVER ###
def GameoverMenu():
    perm_json()
        # Ler o JSON do arquivo
    with open('game_data.json', 'r') as file:
        json_data = file.read()

    # Converter o JSON de volta para um dicionário
    data = json.loads(json_data)

    # Acessar o score e o progresso no dicionário
    score = data['score']
    progress = data['progress']

    file.close()

    os.remove('game_data.json')

    gameover_menu = pygame_menu.Menu(
        title='',
        theme=theme,
        height=menus.WINDOW_SIZE[1] * menus.SIZE,
        width=menus.WINDOW_SIZE[0] * menus.SIZE
    )
    game_score = "Barreiras " + str(progress) + "/20" "\nscore " + str(score)
    gameover_menu.add.label("", font_color=(255, 255, 255), align=pygame_menu.locals.ALIGN_CENTER, font_size=40)
    gameover_menu.add.label(game_score, font_color=(255, 255, 255), align=pygame_menu.locals.ALIGN_CENTER, font_size=40)
    gameover_menu.add.button('Retry', menus.retry)
    gameover_menu.add.button('Quit', pygame_menu.events.EXIT)
    gameover_menu.add.button('Main Menu', menus.back)
    
    gameover_menu.enable()
    gameover_menu.mainloop(menus.DISPLAY)
###

##Victory##
def VictoryMenu():
    perm_json()
        # Ler o JSON do arquivo
    with open('game_data.json', 'r') as file:
        json_data = file.read()

    # Converter o JSON de volta para um dicionário
    data = json.loads(json_data)

    # Acessar o score e o progresso no dicionário
    score = data['score']
    progress = data['progress']

    file.close()
    

    endexits = os.path.exists('game_perm_data.json')
    # Ler o JSON do arquivo
    Endless = False

    if endexits == True:
        with open('game_perm_data.json', 'r') as file:
            json_data = file.read()

            # Converter o JSON de volta para um dicionário
            data = json.loads(json_data)

            # Acessar o score e o progresso no dicionário
            try:
                Endless = data['endless']
            except:
                pass

        file.close()
    os.remove('game_data.json')

    if Endless == False:
        with open('game_perm_data.json', 'r') as file:
            json_data = file.read()

        # Converter o JSON de volta para um dicionário
        data = json.loads(json_data)

        file.close()
            #json
            # Criar um dicionário com o game.score e o progresso
        data["endless"] = True
            # Converter o dicionário em JSON
        json_data = json.dumps(data)

        # Escrever o JSON no arquivo
        with open('game_perm_data.json', 'w') as file:
            file.write(json_data)

        file.close()

    gameover_menu = pygame_menu.Menu(
        title='',
        theme=theme,
        height=menus.WINDOW_SIZE[1] * menus.SIZE,
        width=menus.WINDOW_SIZE[0] * menus.SIZE
    )
    game_score = "Barreiras " + str(progress) + "/20" "\nscore " + str(score)
    gameover_menu.add.label(game_score, font_color=(255, 255, 255), align=pygame_menu.locals.ALIGN_CENTER, font_size=40)
    if Endless == False:
        gameover_menu.add.label("Novo modo liberado", font_color=(255, 255, 255), align=pygame_menu.locals.ALIGN_CENTER, font_size=40)
    gameover_menu.add.button('Retry', menus.retry)
    gameover_menu.add.button('Quit', pygame_menu.events.EXIT)
    gameover_menu.add.button('Main Menu', menus.back)
    gameover_menu.enable()
    gameover_menu.mainloop(menus.DISPLAY)
###

### GAMEOVER ENDLESS ###
def GameoverEndMenu():
    perm_json()
        # Ler o JSON do arquivo
    with open('game_data.json', 'r') as file:
        json_data = file.read()

    # Converter o JSON de volta para um dicionário
    data = json.loads(json_data)

    # Acessar o score e o progresso no dicionário
    score = data['score']
    progress = data['progress']

    file.close()

    os.remove('game_data.json')

    gameover_menu = pygame_menu.Menu(
        title='',
        theme=theme,
        height=menus.WINDOW_SIZE[1] * menus.SIZE,
        width=menus.WINDOW_SIZE[0] * menus.SIZE
    )
    game_score = "Barreiras " + str(progress) + "\nscore " + str(score)
    gameover_menu.add.label(game_score, font_color=(255, 255, 255), align=pygame_menu.locals.ALIGN_CENTER, font_size=40)
    gameover_menu.add.button('Retry', menus.endless)
    gameover_menu.add.button('Quit', pygame_menu.events.EXIT)
    gameover_menu.add.button('Main Menu', menus.back)
    
    gameover_menu.enable()
    gameover_menu.mainloop(menus.DISPLAY)

### game_menu ###
def GameMenu():
    def BackGame():
        pygame.mixer.music.unpause()
        game_menu.disable()

    def BackMenu():
        pygame.mixer.music.stop()
        from menus.interface import MainMenu
        MainMenu()

    game_menu = pygame_menu.Menu(
        title='',
        theme=theme,
        height=menus.WINDOW_SIZE[1] * menus.SIZE,
        width=menus.WINDOW_SIZE[0] * menus.SIZE
    )
    game_menu.add.label("Pause", font_size=50, font_color=(255, 255, 255), font_shadow=True, font_shadow_color=10,
                        margin=(0, 30))
    game_menu.add.button('Resume', BackGame)
    game_menu.add.button('exit', BackMenu)

    game_menu.enable()
    game_menu.mainloop(menus.DISPLAY)

