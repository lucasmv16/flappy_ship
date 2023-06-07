import pygame  # Library for game development in Python
import pygame_menu  # Library for creating menus in pygame
import sys  # System-related functionalities and interactions
import time  # Functions related to time and pauses
import menus  # Custom module for game menus
import os

from menus.texts import *  # Custom module for menu text
from menus.theme import theme, font, theme_title  # Custom module for menu theme and fonts
from menus import retry, back  # Custom modules for retry and back functionality in menus

### MENU STORY ###
def StoryMenu():
    story_menu = pygame_menu.Menu(
        title='',
        theme=theme,
        height=menus.WINDOW_SIZE[1] * menus.SIZE,
        width=menus.WINDOW_SIZE[0] * menus.SIZE
    )

    for m in ABOUT_STORY:
        story_menu.add.label(m, font_size=21, font_color=(255, 255, 0))
    story_menu.add.vertical_margin(30)
    story_menu.add.button('Play', retry)
    story_menu.add.button('Back', MainMenu)

    story_menu.enable()
    story_menu.mainloop(menus.DISPLAY)
###

### Options ###
def OptionMenu():
    option_menu = pygame_menu.Menu(
        title='Options',
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

    option_menu.add.range_slider(
        'Volume Master', 100, (0, 100), 1,
        rangeslider_id='range_slider',
        value_format=lambda x: str(int(x))
    )
    option_menu.add.button('OK', menus.apply)
    option_menu.add.button('Back', MainMenu)

    option_menu.enable()
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
        about_menu.add.label(m, font_size=20, font_color=(255, 255, 255))
    about_menu.add.vertical_margin(30)
    about_menu.add.button('Back', MainMenu)

    about_menu.enable()
    about_menu.mainloop(menus.DISPLAY)
###


### MAIN ###
def MainMenu():
    theme.title_offset = (0, 0)
    main_menu = pygame_menu.Menu(
        title="",
        onclose=pygame_menu.events.EXIT,  # User press ESC button
        theme=theme,
        height=menus.WINDOW_SIZE[1] * menus.SIZE,
        width=menus.WINDOW_SIZE[0] * menus.SIZE
    )
    main_menu.add.label("Flappy Ship", underline=True, font_size=50, font_color=(255, 165, 0), font_shadow=True, font_shadow_color=10,
                        margin=(0, 30))

    main_menu.add.button('Story', StoryMenu)
    main_menu.add.button('Options', OptionMenu)
    main_menu.add.button('About', AboutMenu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)
    
    main_menu.enable()
    main_menu.mainloop(menus.DISPLAY)
###
