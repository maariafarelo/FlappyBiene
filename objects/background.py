from operator import index
import pygame
import assets
import configs


class Background(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        self.image = assets.get_sprites("background")
        self.rect = self.image.get_rect(topleft=(configs.SCREEN_WIDTH * index, 0))
        super().__init__(*groups)

    def update(self):
        self.rect.x -= 1

        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH