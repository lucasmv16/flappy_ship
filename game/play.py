import pygame  # Library for game development in Python
import os
import game
 
from game.draw import draw_itens #draw itens on the screen
from game.shot import shot_move, death_shot #Import shot action 
from game.player_action import player_jump, shooting, pause #Import player action
from game.background import bg_move #Import background action
from game.json import json_score #saving your score on a json
from game.check import fall, roof #checking if player are on the screen and if he didn't die
from game.pre_settings import reset #Getting pre settings for the work
from game.obstacle import generate_obs, new_obs
from pygame.locals import *  # Import constants and events from pygame.locals
from settings.screen import *  # Screen configurations for the game

pygame.init()

def start_game():
    reset()
    json_score()  

    font = pygame.font.Font('freesansbold.ttf', 30)

    ### Function for obstacle respawn ###
    while True:
        game.clock.tick(framerate)
        game.y_player += game.gravity
        game.gravity += 0.35

        generate_obs()

        fall()
        
        roof()

        bg_move()

        # exit
        for event in pygame.event.get():
            if event.type == QUIT:
                os.remove('game_data.json') #delete json
                pygame.quit()
                exit()

            ### Controller ###
            if event.type == KEYDOWN:  
                # Jump
                if event.key == K_SPACE or event.key == K_w:
                    player_jump()

                # Shot
                if event.key == K_e and not game.shot_moven or event.key == K_p and not game.shot_moven:
                    shooting()
                # Pause
                if event.key == pygame.K_ESCAPE:
                    pause()
        
        shot_move()

        if game.pos_x_missil >= game.sw + 31:
            death_shot()
        
        new_obs()

        ### Test zone ###
        if game.progress == 15:
            game.stop_create = True
        if game.progress == 20 and game.vel > 0 and game.i >= 20:
            game.vel -= 1
            game.x_heart -= game.vel_stop
            game.i = 0
        game.i+= 1


        draw_itens()

        ### Write your score on screen ###
        score_text = font.render('Score: ' + str(game.score), True, (255, 255, 255))
        game.screen.blit(score_text, (0, 0))

        ### update screen ###
        pygame.display.update()
