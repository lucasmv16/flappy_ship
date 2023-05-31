import pygame, sys, time, random
from pygame.locals import *
from settings.screen import *
from menus.menu_game import GameoverMenu, GameMenu

pygame.init()

def game():
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
    obstacle = pygame.transform.scale(obstacle, (100,100))

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
    pos_x_missil = sw/1.5 + 31
    pos_y_missil = sh/1.5 + 31
    shot_moven = False
    shot_back = False

    ##shot##
    triggered = False

    ##position obstacle##  
    pos_x_obstacle = ssw
    pos_y_obstacle = 0

    ##player possion##
    x_player = (sw/1.5) / 4
    y_player = (sh/1.5) / 4
    gravity = 0

    ##Function for obstacle respawn##
    while True:
        ##reset##
        clock.tick(framerate)
        screen.fill((0,0,0))
        y_player += gravity
        gravity += 0.35  

        ##fall death##
        if y_player >= max_y_player - 41 and gravity > 0:
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
                    triggered = True
                    vel_x_missil = 10
                    shot_moven = True

                    if shot_back:
                        pos_x_missil = x_player
                        pos_y_missil = y_player
                        shot_back = False

        
        if shot_moven == True:
            pos_x_missil += vel_x_missil #fazendo o tiro ter o movimento

        ##death of shot##
        if pos_x_missil >= ssw + 31:
            shot_back = True
            shot_moven = False
        
        ##wall##
        pos_x_obstacle -= 10

                
        ##shot, player and wall creation##
        screen.blit(missil, (pos_x_missil, pos_y_missil))
        screen.blit(player_nave, (x_player, y_player))
        pygame.draw.rect(screen, (0, 255, 0), (pos_x_obstacle, pos_y_obstacle, 100, ssh/1.75))
        
        ##update screen##
        pygame.display.update()
