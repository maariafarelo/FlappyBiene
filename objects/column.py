import pygame.sprite
import assets
import configs


class Column(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self.gap = 100

        self.sprite = assets.get_sprites("column")
        self.sprite_rect = self.sprite.get_rect()

        self.pipe_bottom = self.sprite
        self.pipe_bottom_rect = self.pipe_bottom.get_rect(topleft=(0,0))

        self.pipe_top = pygame.transform.flip(self.sprite, False, True)
        self.pipe_top_rect = self.pipe_top.get_rect(topleft=(0, 0))

        self.image = pygame.surface.Surface((self.sprite_rect.width, self.sprite_rect.height * 2 + self.gap))
        self.rect = self.image.get_rect(topleft=(300, 0))
        self.image.fill("red")
        self.image.blit(self.pipe_bottom, self.pipe_bottom_rect)
        self.image.blit(self.pipe_top, self.pipe_top_rect)
        super().__init__(*groups)

    #def update(self):
        #self.rect.x -= 1

