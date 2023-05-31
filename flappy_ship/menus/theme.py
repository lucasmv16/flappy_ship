import pygame_menu
from pygame_menu import sound

### Theme ###
font = pygame_menu.font.FONT_8BIT
theme = pygame_menu.themes.THEME_ORANGE.copy()
background = pygame_menu.baseimage.BaseImage(
    image_path="./assets/images/bg-menu.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY,
    drawing_offset=(0,0)
)
theme.widget_font = font
theme.background_color = background
theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE

### SOUNDS ###
##engine = sound.Sound(frequency=44100, uniquechannel=False)
#engine.set_sound(sound.SOUND_TYPE_WIDGET_SELECTION, './assets/sounds/select.ogg')
#engine.set_sound(sound.SOUND_TYPE_OPEN_MENU, './assets/sounds/enter.ogg')
#engine.set_sound(sound.SOUND_TYPE_KEY_ADDITION, './assets/sounds/exit.ogg')
