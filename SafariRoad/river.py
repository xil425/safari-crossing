import pygame

class River:
    SIZE = (600, 20)
    SCREEN_DIM = 600, 500

    def __init__(self, river_height: int, direction: str):
        self.rect = pygame.Rect((0, 50), 300,200)