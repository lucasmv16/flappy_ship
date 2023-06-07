
import pygame  # Library for game development in Python
import sys  # System-related functionalities and interactions
import time  # Functions related to time and pauses
import random  # Functions for generating random numbers
import json  # Handling data in JSON format

from pygame.locals import *  # Import constants and events from pygame.locals
from settings.screen import *  # Screen configurations for the game
from game.music import sound_effects, sound  # Sound effects and game music
from menus.interface_ingame import GameoverMenu, GameMenu  # Game interfaces, such as the game over menu

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

def game():
    sound_effects(sound["soundtrank"])
    def draw_obstalce(obstacle, obst, y_pos , player):
        for i in range(len(obst)):
            y_coord = y_pos[i]
            obstacle = pygame.transform.scale(obstacle, (100,y_coord))
            top_rect = screen.blit(obstacle, [obst[i], 0, 100, y_coord])
            obstacle = pygame.transform.scale(obstacle, (100,ssh - (y_coord + 70)))
            bot_rect = screen.blit(obstacle, [obst[i], y_coord + 275, 100, ssh - (y_coord + 70)])

            if top_rect.colliderect(player) or bot_rect.colliderect(player):
                pygame.mixer.music.stop()
                sound_effects(sound["dead"])
                GameoverMenu()

    ##screen##
    fullscreen = False
    screen = pygame.display.set_mode(((sw/1.5), (sh/1.5)), pygame.RESIZABLE)
    pygame.display.set_caption('Flappy Ship')
    clock = pygame.time.Clock()
    ssw = sw/1.5
    ssh = sh/1.5

    ##background##
    bif = './assets/images/bg-game.jpg'

    bgw = sw/1.5
    bgh = sh/1.5
    bg =  pygame.image.load(bif).convert_alpha()
    bg = pygame.transform.scale(bg, (bgw,bgh))

    ###shot##
    bif = "./assets/images/fire.png"
    missil = pygame.image.load(bif).convert_alpha()
    missil = pygame.transform.scale(missil, (30,30))

    ##Obstacle##
    bif = "./assets/images/pilar.png"
    obstacle = pygame.image.load(bif).convert_alpha()
    new_obstacle = True

    ##img_Nave##
    bif = "./assets/images/nave.png"
    player_nave = pygame.image.load(bif).convert_alpha()
    player_nave = pygame.transform.scale(player_nave, (60,60))
    player_nave = pygame.transform.rotate(player_nave, -90)

    ##player max possion##
    min_y_player = 0
    max_y_player = sh/1.5

    ##shot speed##
    vel_x_missil = 0
    pos_x_missil = -31
    pos_y_missil = -31
    shot_moven = False
    shot_back = True

    ##position obstacle##  
    obstacles = [400, 700, 1000, 1300, 1600]
    generate_places = True
    pos_y_obstacle = []

    ##player possion##
    x_player = (sw/1.5) / 4
    y_player = (sh/1.5) / 4
    gravity = 0

    ##score##
    score = 0
    progress = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    #json
    # Criar um dicionário com o score e o progresso
    data = {
        'score': score,
        'progress': progress
    }

    # Converter o dicionário em JSON
    json_data = json.dumps(data)

    # Escrever o JSON no arquivo
    with open('game_data.json', 'w') as file:
        file.write(json_data)
  

    ##Function for obstacle respawn##
    while True:
        ##reset##
        clock.tick(framerate)
        screen.fill((0,0,0))
        y_player += gravity
        gravity += 0.35  

        if generate_places:
            for i in range(len(obstacles)):
                pos_y_obstacle.append(random.randint(0, ssh - 200))
            generate_places = False

        ##fall death##
        if y_player >= max_y_player - 41 and gravity > 0:
            pygame.mixer.music.stop()
            sound_effects(sound["dead"])
            GameoverMenu()

        ##Background move##
        rel_x = bgw % bg.get_rect().width
        screen.blit(bg, (rel_x - bg.get_rect().width,0)) #criar backgroud
        if rel_x < 2000:  
            screen.blit(bg, (rel_x,0))  
        bgw -= 6 #a velocidade do background

        ##dont pass of screen##
        if y_player <= min_y_player and gravity < 0:
            y_player = min_y_player
            gravity = 0

        ##exit button##
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            
            ##resize the window##
            if event.type == VIDEORESIZE:
                if not fullscreen:         
                    screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    x_player = event.w / 4
                    max_y_player = event.h
                    bgw = event.w
                    bgh = event.h
                    ssw = event.w
                    ssh =event.h
                    bg = pygame.transform.scale(bg, (bgw,bgh))

            ##teclas##
            if event.type == KEYDOWN:  
                ##set fullscreen mode##
                if event.key == K_F11:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((sw, sh), pygame.FULLSCREEN)
                        x_player = sw/4
                        max_y_player = sh
                        bgw = sw
                        bgh = sh
                        ssw = sw
                        ssh = sh
                        bg = pygame.transform.scale(bg, (bgw,bgh))
                    else:
                        screen = pygame.display.set_mode(((sw/1.5), (sh/1.5)), pygame.RESIZABLE)
                        x_player = (sw/1.5)/4
                        max_y_player = sh/1.5
                        bgw = sw/1.5
                        bgh = sh/1.5
                        ssw = sw/1.5
                        ssh = sh/1.5
                        bg = pygame.transform.scale(bg, (bgw,bgh))
                ##Jump##
                if event.key == K_SPACE or event.key == K_w:
                    gravity = 0
                    gravity -= 10

                if event.key == K_e and not shot_moven or event.key == MOUSEBUTTONDOWN and not shot_moven:
                    vel_x_missil = 10
                    shot_moven = True

                    if shot_back:
                        pos_x_missil = x_player
                        pos_y_missil = y_player
                        shot_back = False
                #Pause
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.pause()
                    GameMenu()
        
        if shot_moven == True:
            pos_x_missil += vel_x_missil #fazendo o tiro ter o movimento

        ##death of shot##
        if pos_x_missil >= ssw + 31:
            shot_back = True
            shot_moven = False
        
        for i in range(len(obstacles)):
            obstacles[i] -= 3
            if obstacles[i] <= x_player and new_obstacle == True:
                score += 10
                progress += 1
                new_obstacle = False
                # Criar um dicionário com o score e o progresso
                data = {
                    'score': score,
                    'progress': progress
                }

                # Converter o dicionário em JSON
                json_data = json.dumps(data)

                # Escrever o JSON no arquivo
                with open('game_data.json', 'w') as file:
                    file.write(json_data)

            if obstacles[i] < -100:
                obstacles.remove(obstacles[i])
                pos_y_obstacle.remove(pos_y_obstacle[i])
                obstacles.append(random.randint(obstacles[-1] + 280, obstacles[-1] + 320))
                pos_y_obstacle.append(random.randint(0, int(ssh*0.6)))
                new_obstacle = True


        score_text = font.render('Score: ' + str(score), True, (255, 255, 255))

        ##shot, player and wall creation##
        screen.blit(missil, (pos_x_missil, pos_y_missil))
        player = screen.blit(player_nave, (x_player, y_player))
        draw_obstalce(obstacle, obstacles, pos_y_obstacle, player)
        screen.blit(score_text, (0, 0))

        ##update screen##
        pygame.display.update()