from operator import index

import pygame.sprite

import assets
import configs


class Floor (pygame.sprite.Sprite):
    def __init__(self,index, *groups):

        self.image = assets.get_sprites("floor")
        self.rect = self.image.get_rect(bottomleft=(configs.SCREEN_WIDTH * index,configs.SCREEN_HEIGHT))
        super().__init__(*groups)

    def update(self):
        self.rect.x -= 2

        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH