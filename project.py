import pygame
import sys
import random
import time
import card
import AI

image_size = (200, 200)
cowboy = pygame.image.load("cowboy_hat.png")
fedora = pygame.image.load("fedora.png")
grad_hat = pygame.image.load("graduation-hat.png")
tophat = pygame.image.load("tophat.png")
cowboy = pygame.transform.scale(cowboy, image_size)
fedora = pygame.transform.scale(fedora, (150, 150))
grad_hat = pygame.transform.scale(grad_hat, (200, 120))
tophat = pygame.transform.scale(tophat, (150, 120))


def main():
    # turn on pygame
    pygame.init()
    screen = pygame.display.set_mode((1400, 800))
    pygame.display.set_caption("Poker")
    screen.fill((53, 101, 57))
    cards = card.cardlist()
    clock = pygame.time.Clock()
    game_round = 0
    turn = 1
    ai0 = AI.AI(screen, 0)
    ai1 = AI.AI(screen, 1)
    ai2 = AI.AI(screen, 2)

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
        if round == 5:
            pass


        screen.fill((53, 101, 57))
        for ddd in cards_main_list:
            ddd.draw(game_round)

        screen.blit(grad_hat, (1000, 650))
        ai0.draw()
        ai1.draw()
        ai2.draw()


        pygame.display.update()

main()
