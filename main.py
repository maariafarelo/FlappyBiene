import pygame
import assets
import configs
from objects.background import Background
from objects.column import Column
from objects.floor import Floor

pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

assets.load_sprites()
sprites = pygame.sprite.LayeredUpdates()
Background(0, sprites)
Background(1, sprites)

Floor(0, sprites)
Floor(1, sprites)


Column (sprites)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    sprites.draw(screen)
    sprites.update()
    
    pygame.display.flip()
    clock.tick(configs.FPS)
pygame.quit()
