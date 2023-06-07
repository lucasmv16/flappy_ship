import pygame  # Library for game development and multimedia applications
import pygame_menu  # Library for creating menus in pygame
import json  # Library for working with JSON data
import menus  # Custom module for game menus

from menus.theme import theme  # Custom theme module for menu styling
from menus.theme import font  # Custom module for defining fonts in the menu


### VARS GLOBAL ###


### GAMEOVER ###
def GameoverMenu():
        # Ler o JSON do arquivo
    with open('game_data.json', 'r') as file:
        json_data = file.read()

    # Converter o JSON de volta para um dicionário
    data = json.loads(json_data)

    # Acessar o score e o progresso no dicionário
    score = data['score']
    progress = data['progress']
    gameover_menu = pygame_menu.Menu(
        title='Game Over',
        theme=theme,
        height=menus.WINDOW_SIZE[1] * menus.SIZE,
        width=menus.WINDOW_SIZE[0] * menus.SIZE
    )
    game_score = "Barreiras " + str(progress) + "/20" "\nscore " + str(score)
    gameover_menu.add.label(game_score, font_color=(255, 255, 255), align=pygame_menu.locals.ALIGN_CENTER, font_size=40)
    gameover_menu.add.button('Retry', menus.retry)
    gameover_menu.add.button('Quit', pygame_menu.events.EXIT)
    gameover_menu.add.button('Main Menu', menus.back)
    
    gameover_menu.enable()
    gameover_menu.mainloop(menus.DISPLAY)
###

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
