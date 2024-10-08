import os
import pygame
sprites = {}

def load_sprites():
    path = os.path.join("assets","sprites")
    for file in os.listdir(path):
        sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))


def get_sprites(name):
    return sprites[name]