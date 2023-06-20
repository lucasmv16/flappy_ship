import pygame_menu  # Library for creating menus in Pygame
import os  # Operating system-related functionalities and interactions

from pygame_menu import sound  # Sound module for Pygame Menu


### Theme ###
font = pygame_menu.font.FONT_FIRACODE
theme = pygame_menu.themes.THEME_ORANGE.copy()
background = pygame_menu.baseimage.BaseImage(
    image_path="./assets/images/bg-menu.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY,
    drawing_offset=(0,0)
)
theme.widget_font_color = (128, 128, 128)
theme.widget_font = font
theme.background_color = background
theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE

font_title = pygame_menu.font.FONT_FIRACODE
theme_title = theme
theme_title.widget_font = font_title


