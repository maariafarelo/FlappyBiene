import os
import pygame
assets = {}

def load_sprites():
    path = os.path.join("assets")
    for file in os.listdir(path):
        assets[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))


def get_assets(name):
    return assets[name]