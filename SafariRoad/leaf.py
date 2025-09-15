import pygame

class Leaf (pygame.sprite.Sprite):
    # Define constant values
    IMAGE = pygame.image.load('resources/leafobstacle.png')
    STARTING_POSITION = (300, 180)
    SIZE = (25, 15)
    SCREEN_DIM = 600, 500
    MOVE_DIST = 6

    # Creates a Log object
    def __init__(self, starting_position: tuple, direction: str):
        # Sprite Information
        super().__init__()
        self.image = Leaf.IMAGE
        # Leaf Information
        self.rect = pygame.Rect((0, 0), Leaf.SIZE)
        self.rect.center = starting_position
        self.direction = 'Right'

    def move(self):
        # Leaf is going left
        if self.direction == 'Left':
            self.rect.centerx -= Leaf.MOVE_DIST
            # Leaf has moved off the screen
            if self.rect.right <= 0:
                self.rect.centerx = Leaf.SCREEN_DIM[0] + Leaf.SIZE[0] / 2
        # Leaf is going right
        else:
            self.rect.centerx += Leaf.MOVE_DIST
            # Leaf has moved off the screen
            if self.rect.left >= Leaf.SCREEN_DIM[0]:
                self.rect.centerx = -Leaf.SIZE[0] / 2