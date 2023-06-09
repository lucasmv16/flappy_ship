import pygame  # Library for game development in Python
import os
import game

from game.draw import draw_itens
from game.shot import shot_move, death_shot #Import shot action 
from game.player_action import player_jump, shooting, pause #Import player action
from game.background import bg_move #Import background action
from game.json import json_score #saving your score on a json
from game.check import fall, roof #checking if player are on the screen and if he didn't die
from game.pre_settings import reset #Getting pre settings for the work
from game.obstacle import generate_obs, new_obs
from pygame.locals import *  # Import constants and events from pygame.locals
from settings.screen import *  # Screen configurations for the game

################################################
### POR FAVOR LUCAS LEIA TUDO E FALE COMIGO.####
################################################
# TIRE A FUNÇÃO DRAW_OBSTALCE DE DENTRO DO JOGO
# COLOCA TODAS AS VARS GLOBAL NO __INIT__.
# CRIEI UMA FUNÇÃO PARA DETECTAR SE O JOGADOR -
# MORREU.
# MOVA O LOOP WHILE PARA O MAIN.PY.
# COLOQUE O TIRO DENTRO DE UMA FUNÇÃO.
# ARRUME O BACKGROUND.
# TROQUE ESSA SPRITE DA BARREIRA.
# ENVIE O SCORE E O PROGRESS PARA UM ARQUIVO -
# PARA MIM USAR NO MENU.
# POR FAVOR USE IMPORT.
# TENTE DEMINUIR ESSES IF ELSE.
# USE ELIF E NÃO IF.
# ps. EU POSSO AJUDAR SE VC PEDIR
################################################
#### POR FAVOR LUCAS LEIA CLEAN CODE        ####
################################################

pygame.init()

def start_game():
    reset()
    json_score()  

    font = pygame.font.Font('freesansbold.ttf', 30)

    ##Function for obstacle respawn##
    while True:
        ##reset##
        game.clock.tick(framerate)
        game.y_player += game.gravity
        game.gravity += 0.35  

        generate_obs()

        fall()
        
        roof()

        bg_move()

        ##exit button##
        for event in pygame.event.get():
            if event.type == QUIT:
                os.remove('game_data.json') #delete json
                pygame.quit()
                exit()

            ##teclas##
            if event.type == KEYDOWN:  
                ##Jump##
                if event.key == K_SPACE or event.key == K_w:
                    player_jump()

                ##shooting##
                if event.key == K_e and not game.shot_moven or event.key == K_p and not game.shot_moven:
                    shooting()
                #Pause
                if event.key == pygame.K_ESCAPE:
                    pause()
        
        shot_move()

        death_shot()
        
        new_obs()

        ##test zone##
        
        #############

        draw_itens()

        ##write your score on screen##
        score_text = font.render('Score: ' + str(game.score), True, (255, 255, 255))
        game.screen.blit(score_text, (0, 0))

        ##update screen##
        pygame.display.update()