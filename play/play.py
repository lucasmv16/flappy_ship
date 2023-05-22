import pygame, sys, time
from pygame.locals import *
from settings import *
from sprites import BG

pygame.init()

monitor = [pygame.display.Info().current_h, pygame.display.Info().current_w]
fullscreen = False
tela = pygame.display.set_mode(((sw/1.5), (sh/1.5)), pygame.RESIZABLE)
pygame.display.set_caption('Flappy Ship')
clock = pygame.time.Clock()

x_player = (sw/1.5) / 4
y_player = (sh/1.5) / 4
gravidade = 0

while True:
    clock.tick(framerate)
    tela.fill((0,0,0))
    y_player += gravidade
    gravidade += 0.5

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == VIDEORESIZE:
            if not fullscreen:
                tela = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                x_player = event.w / 4

        if event.type == KEYDOWN:  
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    tela = pygame.display.set_mode((sw, sh), pygame.FULLSCREEN)
                    x_player = sw/4
                else:
                    tela = pygame.display.set_mode(((sw/1.5), (sh/1.5)), pygame.RESIZABLE)
                    x_player = (sw/1.5)/4

            if event.key == K_SPACE or event.key == K_w:
                gravidade = 0
                gravidade -= 10

    pygame.draw.rect(tela, (0, 0, 255), (x_player, y_player, 40, 40))
    pygame.display.update()