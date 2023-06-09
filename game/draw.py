import game

from game.obstacle import draw_obstalce

def draw_itens():
    game.screen.blit(game.missil, (game.pos_x_missil, game.pos_y_missil))
    player = game.screen.blit(game.player_nave, (game.x_player, game.y_player))
    draw_obstalce(player)