import pygame
from settings import *

class BG(pygame.sprite.Sprite):
    def sprite(self, groups):
        super().sprite(groups)
        self.image = pygame.image.load('./img/robot_factory_sprite_background_by_sonicmechaomega999_d9ljsjx-250t.jpg').convert
        self.rect = self.image.get_rect(topleft = (0, 0))