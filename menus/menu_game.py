import pygame
import pygame_menu
import menus
from menus.theme import theme, font

### VARS GLOBAL ###


### GAMEOVER ###
def GameoverMenu():
    score=10
    progress="10/20"
    gameover_menu = pygame_menu.Menu(
        title='Game Over',
        theme=theme,
        height=menus.WINDOW_SIZE[1] * menus.SIZE,
        width=menus.WINDOW_SIZE[0] * menus.SIZE
    )
    gameover_menu.add.label("barreiras: ", align=pygame_menu.locals.ALIGN_CENTER, font_size=40)
    gameover_menu.add.label(progress, align=pygame_menu.locals.ALIGN_CENTER, font_size=40)
    gameover_menu.add.label("Score: ", align=pygame_menu.locals.ALIGN_CENTER, font_size=40)
    gameover_menu.add.label(score, align=pygame_menu.locals.ALIGN_CENTER, font_size=40)
    gameover_menu.add.button('Retry', menus.retry)
    gameover_menu.add.button('Quit', pygame_menu.events.EXIT)
    gameover_menu.add.button('Main Menu', menus.back)
            # Habilitar o menu
    gameover_menu.enable()

    # Iniciar o loop principal do menu
    gameover_menu.mainloop(menus.DISPLAY)
###

### game_menu ###
def GameMenu():
    game_menu = pygame_menu.Menu(
        title='Pause',
        theme=theme,
        height=menus.WINDOW_SIZE[1] * menus.SIZE,
        width=menus.WINDOW_SIZE[0] * menus.SIZE
    )
    game_menu.add.button('back', pygame_menu.events.CLOSE)
            # Habilitar o menu
    game_menu.enable()

    # Iniciar o loop principal do menu
    game_menu.mainloop(menus.DISPLAY)
