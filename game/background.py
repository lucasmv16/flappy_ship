import game

def bg_move():
    rel_x = game.bgw % game.bg.get_rect().width
    game.screen.blit(game.bg, (rel_x - game.bg.get_rect().width,0)) #criar backgroud
    if rel_x < 2000:  
        game.screen.blit(game.bg, (rel_x,0)) 
    if game.vel != 0:
        game.bgw -= game.vel - 1#a velocidade do background