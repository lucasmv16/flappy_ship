import game
import pygame

from game.shot import shot_collision
from game.obstacle import draw_obstalce
from settings.screen import *

def draw_itens():
    shot = game.screen.blit(game.missil, (game.pos_x_missil, game.pos_y_missil))
    player = game.screen.blit(game.player_nave, (game.x_player, game.y_player))
    heart = pygame.draw.rect(game.screen, (0, 0, 0), (game.x_heart, (sh-500)/2, 500, 500))
    draw_obstalce(player, shot)
    shot_collision(shot, heart)
