import pygame

class Treee (pygame.sprite.Sprite):
    # Define constant values
    IMAGE = pygame.image.load('resources/treeobstacle2.png')
    STARTING_POSITION = (300, 390)
    SIZE = (30, 50)
    SCREEN_DIM = 600, 500
    MOVE_DIST = 4

    # Creates a Tree object
    def __init__(self, starting_position: tuple, direction: str):
        # Sprite Information
        super().__init__()
        self.image = Treee.IMAGE
        # Tree Information
        self.rect = pygame.Rect((0, 0), Treee.SIZE)
        self.rect.center = starting_position
        self.direction = direction

    def move(self):
        # Tree is going left
        if self.direction == 'Left':
            self.rect.centerx -= Treee.MOVE_DIST
            # Tree has moved off the screen
            if self.rect.right <= 0:
                self.rect.centerx = Treee.SCREEN_DIM[0] + Treee.SIZE[0] / 2
        # Tree is going right
        else:
            self.rect.centerx += Treee.MOVE_DIST
            # Log has moved off the screen
            if self.rect.left >= Treee.SCREEN_DIM[0]:
                self.rect.centerx = -Treee.SIZE[0] / 2