import pygame, sys, time
from pygame.locals import *
from settings import *
from sprites import BG

pygame.init()


##screen##
fullscreen = False
screen = pygame.display.set_mode(((sw/1.5), (sh/1.5)), pygame.RESIZABLE)
pygame.display.set_caption('Flappy Ship')
clock = pygame.time.Clock()

##background##
bif = 'play/img/bgg.jpg'

bgw = sw/1.5
bgh = sh/1.5
bg =  pygame.image.load(bif).convert_alpha()
bg = pygame.transform.scale(bg, (bgw,bgh))

###shot##
bif = "play/img/fire.png"
missil = pygame.image.load(bif).convert_alpha()
missil = pygame.transform.scale(missil, (30,30))

##Obstacle##
#bif = "play/img/pillar.png"
#obstacle = pygame.image.load(bif).convert_alpha()
#obstacle = pygame.transform.scale(obstacle, (50,50))

##img_Nave##
bif = "play/img/nave.png"
player_nave = pygame.image.load(bif).convert_alpha()
player_nave = pygame.transform.scale(player_nave, (60,60))
player_nave = pygame.transform.rotate(player_nave, -90)

##player max possion##
min_y_player = 0
max_y_player = sh/1.5

##shot speed##
vel_x_missil = 0
pos_x_missil = 200
pos_y_missil = 300

##shot##
triggered = False

##player possion##
x_player = (sw/1.5) / 4
y_player = (sh/1.5) / 4
gravity = 0

while True:
    ##reset##
    clock.tick(framerate)
    screen.fill((0,0,0))
    y_player += gravity
    gravity += 0.35  

    ##fall death##
    if y_player >= max_y_player - 41 and gravity > 0:
        pygame.quit()
        exit()
        pass
    
    
    screen.blit(bg, (0,0))

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
                    bg = pygame.transform.scale(bg, (bgw,bgh))
                else:
                    screen = pygame.display.set_mode(((sw/1.5), (sh/1.5)), pygame.RESIZABLE)
                    x_player = (sw/1.5)/4
                    max_y_player = sh/1.5
                    bgw = sw/1.5
                    bgh = sh/1.5
                    bg = pygame.transform.scale(bg, (bgw,bgh))
            ##Jump##
            if event.key == K_SPACE or event.key == K_w:
                gravity = 0
                gravity -= 10
                
                

            


            ##Shot##
             

            
    ##blue square##
    #screen.blit(missil, (pos_x_missil, pos_y_missil))
    screen.blit(player_nave, (x_player, y_player))
    
    ##update screen##
    pygame.display.update()


##foto da imagem do missil
#
#
#
##velocidade do missil
#
##crinado imagem
#screen.blit(missil,(pos_x_missil,pos_y_missil))
#screen.blit(playimg,(x_player,y_player))
#
#
##tecla do tiro
#tecla = pygame.key.get_pressed()
#if tecla[pygame.K_UP] and y_player > 1:
#    y_player -=1
#    pos_y_missil -=1
#
#if tecla[pygame.K_DOMW] and y_player > 650:
#    y_player -=1
#
#    if not triggered:
#        pos_y_missil -=1 #para ele ter mobvimento proprio
#
#
##tecla do tiro
#if tecla[pygame.K_SPACE]:
#    triggered = True
#    vel_x_missil = 2
#
##movimento do missil
#pos_x_missil += vel_x_missil
#
#
##respawm do missil
#def respawn_missil():
#    triggered = False
#    respawn_missil_x = x_player
#    respawn_missil_y = y_player
#    vel_x_missil = 0
#    return [respawn_missil_x, respawn_missil_y, triggered, vel_x_missil]
#
#
#if pos_x_missil == 300:
#    pos_x_missil, pos_y_missil, triggered, vel_x_missil = respawn_missil()
#
#
##aqui eles vão para de ser apenas imagens e vão começa a relamente ser objetos
#player_rect = playimg.get_rect()
#pilar_rect = pilar.get_rect()
#missil_rect= missil.get_rect()
#
## aqui vai forma um retangulo para de referencia de como vai ser, e iso vai ter que fica dentro do loop
#
#player_rect.y = y_player
#player_rect.x = x_player
#
#missil_rect.x = pos_x_missil
#missil_rect.y = pos_y_missil
#
#pilar_rect.x = pilar_x
#pilar_react.y = pilar_y
#
#pygame.draw.rect(screen, (255, 0, 0), missil_rect 4)
#pygame.draw.rect(screen, (255, 0, 0), player_rect 4)
#pygame.draw.rect(screen, (255, 0, 0), pilar_rect 4)
#
##função para criar a colissão
#
#def colisions():
#    global score
#    if player_rect.colliderect(pilar_rect):
#        break
#        menu() #aqui to pensado em quanto tiver a colissão entre a nave e o menu para o jogo e ir direto para o menu
#    elif missil_rect.colliderect(pilar_rect):
#        score += 1
#        return True #aqui se tiver a parade que quebra vamos fazer o play ganha mais pontos por ter quebrando ela
#    else:
#        return False
#
##colocar a musica no jogo, barulho do missil, nave, musica de fundo
#pygame.mixer.music.load()