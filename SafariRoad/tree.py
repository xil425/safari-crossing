import pygame

class Tree (pygame.sprite.Sprite):
    IMAGE = pygame.image.load('resources/treeobstacle.png')
    STARTING_POSITION = (300, 320)
    SIZE = (30, 50)
    SCREEN_DIM = 600, 500
    MOVE_DIST = 3

    def __init__(self, starting_position: tuple, direction: str):
        super().__init__()
        self.image = Tree.IMAGE if direction == 'Left' else Tree.IMAGE
        self.rect = pygame.Rect((0, 0), Tree.SIZE)
        self.rect.center = Tree.STARTING_POSITION
        self.direction = direction

    def move(self):
        if self.direction == 'Left':
            self.rect.centerx -= Tree.MOVE_DIST
            #reset
            if self.rect.right <= 0:
                self.rect.centerx = Tree.SCREEN_DIM[0] + (Tree.SIZE[0] / 2)
        else:
            self.rect.centerx += Tree.MOVE_DIST
            #reset
            if self.rect.left >= Tree.SCREEN_DIM[0]:
                self.rect.centerx = Tree.SIZE[0] / 2