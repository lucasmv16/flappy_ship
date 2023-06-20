import pygame  # Library for game development in Python
import pygame_menu  # Library for creating menus in pygame
import sys  # System-related functionalities and interactions
import time  # Functions related to time and pauses
import menus  # Custom module for game menus
import os
import json

from menus.texts import *  # Custom module for menu text
from menus.theme import theme, font, theme_title  # Custom module for menu theme and fonts
from menus import retry, back, endless  # Custom modules for retry and back functionality in menus

### MENU STORY ###
def StoryMenu():
    story_menu = pygame_menu.Menu(
        title='',
        theme=theme,
        height=menus.WINDOW_SIZE[1] * menus.SIZE,
        width=menus.WINDOW_SIZE[0] * menus.SIZE
    )

    for m in ABOUT_STORY:
        story_menu.add.label(m, font_size=21, font_color=(255, 255, 0))
    story_menu.add.vertical_margin(30)
    story_menu.add.button('Play', retry)
    story_menu.add.button('Back', MainMenu)

    story_menu.enable()
    story_menu.mainloop(menus.DISPLAY)
###

### Options ###
def OptionMenu():
    option_menu = pygame_menu.Menu(
        title='Options',
        theme=theme,
        height=menus.WINDOW_SIZE[1] * menus.SIZE,
        width=menus.WINDOW_SIZE[0] * menus.SIZE
    )
    selector_screen = option_menu.add.dropselect(
        title='Resolution',
        items=[('1280x720 (hd)', 0)],
        font_size=23,
        default=0,
    )

    option_menu.add.range_slider(
        'Volume Master', 100, (0, 100), 1,
        rangeslider_id='range_slider',
        value_format=lambda x: str(int(x))
    )
    option_menu.add.button('OK', menus.apply)
    option_menu.add.button('Reset all data', reset_all)
    option_menu.add.button('Back', MainMenu)

    option_menu.enable()
    option_menu.mainloop(menus.DISPLAY)
###

def reset_all():
    try:
        os.remove('game_perm_data.json')
        MainMenu()
    except:
        MainMenu()

### Class Score
class Score:
    def __init__(self, game_scores): # inicialização da classe
        self.scores = game_scores    # colocando o valor de score dentro de var self
        self.score_menu = pygame_menu.Menu(title='', # iniciando metodo menu
                                           theme=theme,
                                           height=menus.WINDOW_SIZE[1] * menus.SIZE,
                                           width=menus.WINDOW_SIZE[0] * menus.SIZE)
    def create_list_score(self):     # metodo para formatar a var
        display_score = [(indice + 1, score) for indice, score in enumerate(self.scores)]
        return display_score

    def display_menu(self):          # metodo cria os widgets e inicia o menu
        self.score_menu.add.label('Score',margin=(0,20), font_color=(255, 255, 255), font_size=40)
        scores = self.create_list_score()    # recebendo a lista de tuplas
        for rank, score in scores:           # for para mostrar todas as tuplas
            self.score_menu.add.label(f"{rank}- {score}", font_size=36, font_color=(255,255,255), align=pygame_menu.locals.ALIGN_CENTER)

        self.score_menu.add.button('Ok', MainMenu) # botão para voltar
        self.score_menu.add.button('Reset Score', reset_score) # botão para resetar o score
        self.score_menu.enable()                   # Loop do menu
        self.score_menu.mainloop(menus.DISPLAY)    # loop do menu

def reset_score():
    endexits = os.path.exists('game_perm_data.json')
    if endexits == True:
        with open('game_perm_data.json', 'r') as file:
            json_data = file.read()

        # Converter o JSON de volta para um dicionário
        data = json.loads(json_data)

        file.close()

        try:
            data.pop("score", None)
        except:
            pass
        # Converter o dicionário em JSON
        json_data = json.dumps(data)

        # Escrever o JSON no arquivo
        with open('game_perm_data.json', 'w') as file:
            file.write(json_data)

        file.close()
    MainMenu()
### ABOUT ###
def AboutMenu():
    about_menu = pygame_menu.Menu(
        title="About",
        theme=theme,
        height=menus.WINDOW_SIZE[1] * menus.SIZE,
        width=menus.WINDOW_SIZE[0] * menus.SIZE
    )
    for m in ABOUT:
        about_menu.add.label(m, font_size=20, font_color=(255, 255, 255))
    about_menu.add.vertical_margin(30)
    about_menu.add.button('Back', MainMenu)

    about_menu.enable()
    about_menu.mainloop(menus.DISPLAY)
###


### MAIN ###
def MainMenu():
    endexits = os.path.exists('game_perm_data.json')
    # Ler o JSON do arquivo
    Endless = False
    data = {}
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

    theme.title_offset = (0, 0)
    main_menu = pygame_menu.Menu(
        title="",
        onclose=pygame_menu.events.EXIT,  # User press ESC button
        theme=theme,
        height=menus.WINDOW_SIZE[1] * menus.SIZE,
        width=menus.WINDOW_SIZE[0] * menus.SIZE
    )
    main_menu.add.label("Flappy Ship", underline=True, font_size=50, font_color=(255, 165, 0), font_shadow=True, font_shadow_color=10,
                        margin=(0, 30))

    # Exenplo de como usar o menu de score
    try:
        score_player = data["score"]     # var temp para simular scores dos jogadores
    except:
        score_player = []
    score_menu = Score(score_player)         # criando uma instancia com o var scores
    #
    
    main_menu.add.button('Story', StoryMenu)
    if Endless == True:
        main_menu.add.button('Endless', endless)
    main_menu.add.button('Options', OptionMenu)
    main_menu.add.button('Score', score_menu.display_menu) # Iniciando o metodo display_menu, inicia o menu
    main_menu.add.button('About', AboutMenu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)
    
    main_menu.enable()
    main_menu.mainloop(menus.DISPLAY)
###
