import pygame, sys
from giraffe import Giraffe
from tree import Tree
from treee import Treee
from bush import Bush
from leaf import Leaf
from lion import Lion

pygame.init()
pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])

#screen display
SCREEN_DIM = WIDTH, HEIGHT = 600, 500
SCREEN = pygame.display.set_mode(SCREEN_DIM)
pygame.display.set_caption("Giraffe Safari!")
CLOCK = pygame.time.Clock()
FPS = 60

#colors
GROUND_YELLOW = (199, 169, 107)
BACKGROUND_BLUE = (109, 182, 234)
WORD_BROWN = (78, 45, 10)
GREEN = (109, 147, 83)
WORD_GREEN = (191, 198, 124)
MENU_BROWN = (172, 146, 88)
FONT = pygame.font.Font('resources/font.ttf', 18)
MENU_BIG = pygame.font.Font('resources/font.ttf', 48)
MENU_MED = pygame.font.Font('resources/font.ttf', 25)
MENU_SMALL = pygame.font.Font('resources/font.ttf', 15)
MENU_IMAGE = pygame.image.load('resources/menuimage.png')
MENU_IMAGE2 = pygame.image.load('resources/menuimage2.png')

START_MENU = True
END_MENU = False

giraffe = Giraffe()
tree = Tree(Tree.STARTING_POSITION, 'Left')
treee = Treee(Treee.STARTING_POSITION, 'Right')
bush = Bush(Bush.STARTING_POSITION, 'Left')
leaf = Leaf(Leaf.STARTING_POSITION, 'Right')
lion = Lion(Lion.STARTING_POSITION, 'Left')
score = 0
current_best = 0
high_score = 0

#important loop
while True:
    CLOCK.tick(FPS)
    SCREEN.fill(GROUND_YELLOW)

    #move arrows
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:  # W
                giraffe.move_up()
            if event.key == pygame.K_a:  # A
                giraffe.move_left()
            if event.key == pygame.K_s:  # S
                giraffe.move_down()
            if event.key == pygame.K_d:  # D
                giraffe.move_right()

    # scoring
    if 425 - giraffe.rect.top > current_best:
        current_best = 425 - giraffe.rect.top

    if score + current_best >= high_score:
        high_score = score + current_best

    if giraffe.rect.top <= 15:
        giraffe.reset_position()
        giraffe.lives += 1
        score += 1000 + current_best
        current_best = 0
        print("Score: " + str(score + current_best))
        print("High Score: " + str(high_score))
        print("Lives: " + str(giraffe.lives))

    #font
    score_text = FONT.render("Score: " + str(score + current_best), True, WORD_BROWN)
    high_score_text = FONT.render("High Score: " + str(high_score), True, WORD_BROWN)
    lives_text = FONT.render("Lives: " + str(giraffe.lives), True, WORD_BROWN)
    SCREEN.blit(score_text, (5, 0))
    SCREEN.blit(high_score_text, (5, 20))
    SCREEN.blit(lives_text, (5, 40))

    #menu screen
    while START_MENU:
        CLOCK.tick(15)
        SCREEN.fill(MENU_BROWN)
        name = MENU_BIG.render('GIRAFFE SAFARI', True, WORD_BROWN)
        instructions = MENU_MED.render('Press Space To Start', True, WORD_BROWN)
        SCREEN.blit(name, (25, 130))
        SCREEN.blit(instructions, (100, 210))
        SCREEN.blit(MENU_IMAGE, (170, 250))
        SCREEN.blit(MENU_IMAGE2, (193, 201))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    START_MENU = False

    #end screen
    while END_MENU:
        CLOCK.tick(15)
        SCREEN.fill(GREEN)
        thx = MENU_MED.render('Thanks for Playing!', True, WORD_GREEN)
        scores = MENU_MED.render('Your Final Score: %d' % (score + current_best), True, WORD_GREEN)
        instructions = MENU_SMALL.render('Press \'Space\' To Play Again', True, WORD_GREEN)
        SCREEN.blit(thx, (85, 120))
        SCREEN.blit(scores, (70, 180))
        SCREEN.blit(instructions, (130, 240))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    END_MENU = False
                    current_best = 0
                    score = 0
                    giraffe.lives = 3

        pygame.display.update()

        #collisions
    if giraffe.rect.colliderect(tree.rect):
        giraffe.reset_position()

    if giraffe.rect.colliderect(treee.rect):
        giraffe.reset_position()

    if giraffe.rect.colliderect(bush.rect):
        giraffe.reset_position()

    if giraffe.rect.colliderect(leaf.rect):
        giraffe.move_on_leaf(leaf)

    if giraffe.rect.colliderect(lion.rect):
        giraffe.reset_position()

    tree.move()
    treee.move()
    bush.move()
    leaf.move()
    lion.move()
    SCREEN.blit(tree.image, tree.rect)
    SCREEN.blit(treee.image, treee.rect)
    SCREEN.blit(bush.image, bush.rect)
    pygame.draw.rect(SCREEN, BACKGROUND_BLUE, (0, 190, 600, 55))
    SCREEN.blit(leaf.image, leaf.rect)
    SCREEN.blit(lion.image, lion.rect)
    SCREEN.blit(giraffe.image, giraffe.rect)
    if giraffe.lives == 0:
        END_MENU = True
    pygame.display.flip()

pygame.quit()

