import pygame

class Bush (pygame.sprite.Sprite):
    # Define constant values
    IMAGE = pygame.image.load('resources/bushobstacle.png')
    STARTING_POSITION = (300, 320)
    SIZE = (40, 20)
    SCREEN_DIM = 600, 500
    MOVE_DIST = 5

    def __init__(self, starting_position: tuple, direction: str):
        super().__init__()
        self.image = Bush.IMAGE if direction == 'Left' else Bush.IMAGE
        self.rect = pygame.Rect((0, 0), Bush.SIZE)
        self.rect.center = Bush.STARTING_POSITION
        self.direction = direction

    def move(self):
        # Obstacle is going left
        if self.direction == 'Left':
            self.rect.centerx -= Bush.MOVE_DIST
            # Obstacle has moved off the screen
            if self.rect.right <= 0:
                self.rect.centerx = Bush.SCREEN_DIM[0] + Bush.SIZE[0] / 2