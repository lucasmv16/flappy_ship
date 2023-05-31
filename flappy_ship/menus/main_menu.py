import pygame, sys, time
import pygame_menu
import menus
from menus.texts import *
from menus.theme import theme, font
from menus import retry, back

### Start Pygame init ###
pygame.init()
###

######### MENUS #########

### MENU STORY ###
def StoryMenu():
    story_menu = pygame_menu.Menu(
        title='Story',
        theme=theme,
        height=menus.WINDOW_SIZE[1] * menus.SIZE,
        width=menus.WINDOW_SIZE[0] * menus.SIZE
    )

    for m in ABOUT_STORY:
        story_menu.add.label(m, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
    story_menu.add.vertical_margin(30)
    story_menu.add.button('Play', retry)
    story_menu.add.button('Back', MainMenu)
            # Habilitar o menu
    story_menu.enable()

    # Iniciar o loop principal do menu
    story_menu.mainloop(menus.DISPLAY)
###

### SUBMENU ENDLESS ###
def EndlessSubMenu():
    endless_submenu = pygame_menu.Menu(
        title='About',
        theme=theme,
        height=menus.WINDOW_SIZE[1] * menus.SIZE,
        width=menus.WINDOW_SIZE[0] * menus.SIZE
    )
    for m in ABOUT_ENDLESS:
        endless_submenu.add.label(m, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
    endless_submenu.add.button('Back', EndlessMenu)
    endless_submenu.enable()
    endless_submenu.mainloop(menus.DISPLAY)
###

### MENU ENDLESS ###
def EndlessMenu():
    endless_menu = pygame_menu.Menu(    
        title='Endless',
        theme=theme,
        height=menus.WINDOW_SIZE[1] * menus.SIZE,
        width=menus.WINDOW_SIZE[0] * menus.SIZE
    )
    endless_menu.add.button('Play', retry)
    endless_menu.add.button('About Endless', EndlessSubMenu)
    endless_menu.add.button('Back', MainMenu)
                # Habilitar o menu
    endless_menu.enable()

    # Iniciar o loop principal do menu
    endless_menu.mainloop(menus.DISPLAY)
###

### MENU STATS ###
def StatsMenu():
    stats_menu = pygame_menu.Menu(    
        title='stats',
        theme=theme,
        height=menus.WINDOW_SIZE[1] * menus.SIZE,
        width=menus.WINDOW_SIZE[0] * menus.SIZE
    )

    stats_menu.add.label(menus.PLAYER, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
    stats_menu.add.vertical_margin(30)
    #stats_menu quantas partidas ja jogou
    #stats_menu Maximo de barreiras que passou

    stats_menu.add.button('Back', MainMenu)
    stats_menu.enable()
    stats_menu.mainloop(menus.DISPLAY)
###

### SHOP ###
def ShopMenu():
    shop_menu = pygame_menu.Menu(
        title='Shop',
        theme=theme,
        height=menus.WINDOW_SIZE[1] * menus.SIZE,
        width=menus.WINDOW_SIZE[0] * menus.SIZE
    )
    shop_menu.add.button('Back', MainMenu)
                # Habilitar o menu
    shop_menu.enable()

    # Iniciar o loop principal do menu
    shop_menu.mainloop(menus.DISPLAY)
###

### Options ###
def OptionMenu():
    option_menu = pygame_menu.Menu(
        title='Tutorial',
        theme=theme,
        height=menus.WINDOW_SIZE[1] * menus.SIZE,
        width=menus.WINDOW_SIZE[0] * menus.SIZE
    )
    selector_screen = option_menu.add.dropselect(
        title='Resolution',
        items=[('1920x1080', 0),
                ('1280x720', 1),
                ('1366x768', 2),],
        font_size=23,
        default=1,
    )
    x=""
    option_menu.add.range_slider(
        'Volume Master', 100, (0, 100), 1,
        rangeslider_id='range_slider',
        value_format=lambda x: str(int(x))
    )

    option_menu.add.button('OK', menus.apply, align=pygame_menu.locals.ALIGN_LEFT)
    option_menu.add.button('Back', MainMenu)

            # Habilitar o menu
    option_menu.enable()

    # Iniciar o loop principal do menu
    option_menu.mainloop(menus.DISPLAY)
###

### ABOUT ###
def AboutMenu():
    about_menu = pygame_menu.Menu(
        title="About",
        theme=theme,
        height=menus.WINDOW_SIZE[1] * menus.SIZE,
        width=menus.WINDOW_SIZE[0] * menus.SIZE
    )
    for m in ABOUT:
        about_menu.add.label(m, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
    about_menu.add.vertical_margin(30)
    about_menu.add.button('Back', MainMenu)
            # Habilitar o menu
    about_menu.enable()

    # Iniciar o loop principal do menu
    about_menu.mainloop(menus.DISPLAY)
###


### MAIN ###
def MainMenu():
    main_menu = pygame_menu.Menu(
        title="Flappy Ship",
        onclose=pygame_menu.events.EXIT,  # User press ESC button
        theme=theme,
        height=menus.WINDOW_SIZE[1] * menus.SIZE,
        width=menus.WINDOW_SIZE[0] * menus.SIZE
    )
    main_menu.add.button('Story', StoryMenu)
    main_menu.add.button('Endless', EndlessMenu)
    main_menu.add.button('Stats', StatsMenu)
    main_menu.add.button('Shop', ShopMenu)
    main_menu.add.button('Options', OptionMenu)
    main_menu.add.button('About', AboutMenu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)
    main_menu.title_offset = (10, 10)
    #main_menu.set_sound(engine, recursive=True)
        # Habilitar o menu
    main_menu.enable()

    # Iniciar o loop principal do menu
    main_menu.mainloop(menus.DISPLAY)
###
