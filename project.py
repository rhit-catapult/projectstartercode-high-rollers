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
    cards = card.cardlist()
    clock = pygame.time.Clock()
    game_round = 0

    cards_main_list = []
    for k in range(13):
        cards_main_list.append(card.Card(screen, k, cards))

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_round += 1
                print(game_round)

        screen.fill((53, 101, 57))
        for ddd in cards_main_list:
            ddd.draw(game_round)

        pygame.display.update()

main()
