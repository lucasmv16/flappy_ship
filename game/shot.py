import game

def shot_move():
    if game.shot_moven == True:
            game.pos_x_missil += game.vel_x_missil #fazendo o tiro ter o movimento

def death_shot():
    ##death of shot##
    if game.pos_x_missil >= game.sw + 31:
        game.shot_back = True
        game.shot_moven = False
