import pygame
import sys
import random
import time
import card



def main():
    # turn on pygame
    pygame.init()
    screen = pygame.display.set_mode((1400, 800))
    pygame.display.set_caption("Poker")
    screen.fill((53, 101, 57))
    card.cardlist()
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
