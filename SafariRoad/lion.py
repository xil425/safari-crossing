import pygame

class Lion(pygame.sprite.Sprite):
    # Define constant values
    IMAGE = pygame.image.load('resources/lionobstacle.png')
    STARTING_POSITION = (300, 100)
    SIZE = (20, 35)
    SCREEN_DIM = 600, 500
    MOVE_DIST = 7

    def __init__(self, starting_position: tuple, direction: str):
        # Sprite Information
        super().__init__()
        self.image = Lion.IMAGE
        # Tree Information
        self.rect = pygame.Rect((0, 0), Lion.SIZE)
        self.rect.center = starting_position
        self.direction = direction

    def move(self):
        # Obstacle is going left
        if self.direction == 'Left':
            self.rect.centerx -= Lion.MOVE_DIST
            # Obstacle has moved off the screen
            if self.rect.right <= 0:
                self.rect.centerx = Lion.SCREEN_DIM[0] + Lion.SIZE[0] / 2
        # Obstacle is going right
        else:
            self.rect.centerx += Lion.MOVE_DIST
            # Obstacle has moved off the screen
            if self.rect.left >= Lion.SCREEN_DIM[0]:
                self.rect.centerx = -Lion.SIZE[0] / 2