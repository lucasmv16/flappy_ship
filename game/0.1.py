import pygame, sys, time
from pygame.locals import *
from settings.background import *
from settings.screen import *
from menus.menu_game import GameoverMenu, GameMenu



pygame.init()
pygame.display.set_caption('Flappy Ship')

def game():
    menu_open = False
    screen = pygame.display.set_mode(((sw/1.5), (sh/1.5)), pygame.RESIZABLE)
    fullscreen = False
    clock = pygame.time.Clock()

    min_y_player = 0
    max_y_player = sh/1.5

    x_player = (sw/1.5) / 4
    y_player = (sh/1.5) / 4
    gravity = 0
    running = True

    while running:
        clock.tick(framerate)
        screen.fill((0,0,0))
        y_player += gravity
        gravity += 0.5

        if y_player >= max_y_player - 41 and gravity > 0:
            GameoverMenu()

        if y_player <= min_y_player and gravity < 0:
            y_player = min_y_player
            gravity = 0

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            
            if event.type == VIDEORESIZE:
                if not fullscreen:
                    screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    x_player = event.w / 4
                    max_y_player = event.h

            if event.type == KEYDOWN:  
                if event.key == K_F11:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((sw, sh), pygame.FULLSCREEN)
                        x_player = sw/4
                        max_y_player = sh
                    else:
                        screen = pygame.display.set_mode(((sw/1.5), (sh/1.5)), pygame.RESIZABLE)
                        x_player = (sw/1.5)/4
                        max_y_player = sh/1.5

                if event.key == K_SPACE or event.key == K_w:
                    gravity = 0
                    gravity -= 10
                
                elif event.key == K_ESCAPE:
                    pass

        pygame.draw.rect(screen, (0, 0, 255), (x_player, y_player, 40, 40))
        pygame.display.update()

