import pygame
import sys
import random
import time
suits = ["Hearts", "Clubs", "Diamonds", "Spades"]

for suit in suits:
    img_Kings = pygame.image.load("/Cards/card" + suit + "K.png")
    img_Queens = pygame.image.load("/Cards/card" + suit + "Q.png")
    img_Jacks = pygame.image.load("/Cards/card" + suit + "J.png")
    img_Aces = pygame.image.load("/Cards/card" + suit + "A.png")
    for i in range(2, 10):
        Numerical_Cards = pygame.image.load("/images/card" + suit + str(i) + ".png")

def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("Cool Project")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((840, 680))


    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # TODO: Add you events code

        # TODO: Fill the screen with whatever background color you like!
        screen.fill((53, 101, 57))


        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

main()
