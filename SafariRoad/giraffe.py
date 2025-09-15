import pygame
from leaf import Leaf

class Giraffe (pygame.sprite.Sprite):
    STARTING_POSITION = (300, 445)
    SIZE = (15,40)
    IMAGE = pygame.image.load("resources/giraffe.png")
    MOVE_DIST = 15
    SCREEN_DIM = 600,500

    #creates giraffe
    def __init__(self):
        #sprite setup
        super().__init__()
        self.image = Giraffe.IMAGE
        #giraffe rectangle
        self.rect = pygame.Rect((0, 0), Giraffe.SIZE)
        self.rect.center = Giraffe.STARTING_POSITION
        #lives
        self.lives = 3

    def reset_position(self):
        self.rect.center = Giraffe.STARTING_POSITION
        self.lives -= 1

    #moving up
    def move_up(self):
        if self.rect.top >= 20:
            self.rect.centery -= Giraffe.MOVE_DIST

    #moving down
    def move_down(self):
        if self.rect.bottom <= Giraffe.SCREEN_DIM[1] - 20:
            self.rect.centery += Giraffe.MOVE_DIST

    # moving right
    def move_right(self):
        if self.rect.right <= Giraffe.SCREEN_DIM[0] - 20:
            self.rect.centerx += Giraffe.MOVE_DIST

    #moving left
    def move_left(self):
        if self.rect.left >= 20:
            self.rect.centerx -= Giraffe.MOVE_DIST

    # loop
    def move_on_leaf(self, leaf: Leaf):
        # Leaf moving right
        if leaf.direction == 'Right':
            self.rect.centerx = leaf.rect.centerx + 22
            self.rect.centery = leaf.rect.centery - 12
            # Giraffe has moved off screen
            if self.rect.left >= Leaf.SCREEN_DIM[0]:
                Giraffe.reset_position(self)
        # Leaf moving left
        else:
            self.rect.centerx -= Leaf.MOVE_DIST
            # Giraffe has moved off screen
            if self.rect.right <= 0:
                Giraffe.reset_position(self)