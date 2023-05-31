import pygame
import settings.screen
import sys

sys.dont_write_bytecode = True

class BG(pygame.sprite.Sprite):
    def sprite(self, groups):
        super().sprite(groups)
        self.image = pygame.image.load('./img/robot_factory_sprite_background_by_sonicmechaomega999_d9ljsjx-250t.jpg').convert
        self.rect = self.image.get_rect(topleft = (0, 0))