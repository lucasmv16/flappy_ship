import os  # Operating system-related functionalities and interactions

from pygame import mixer  # Audio mixer module for pygame

sound = {
    'soundtrank': "soundtrank.ogg", 
    'dead': "explosion.ogg",
    'shot': "shot.ogg",
    'hit': "hit.ogg", 
    'ship': "ship.ogg"
}

def sound_effects(sound):
    mixer.init()
    mixer.music.load(os.path.join("assets/sounds", sound))
    mixer.music.set_volume(0.2)
    mixer.music.play()
