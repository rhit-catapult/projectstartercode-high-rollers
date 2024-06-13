import pygame
import sys
import random
import time
import card
import AI
import chip_counter
import handvalue
import human

image_size = (200, 200)
cowboy = pygame.image.load("cowboy_hat.png")
fedora = pygame.image.load("fedora.png")
tophat = pygame.image.load("tophat.png")
cowboy = pygame.transform.scale(cowboy, image_size)
fedora = pygame.transform.scale(fedora, (150, 150))
tophat = pygame.transform.scale(tophat, (150, 120))
pokerchip = pygame.image.load("poker_chip.png")
poker_chip = pygame.transform.scale(pokerchip,(150,150))


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
    player = human.Human(screen)
    ai0 = AI.AI(screen, 0)
    ai1 = AI.AI(screen, 1)
    ai2 = AI.AI(screen, 2)
    players_chips = chip_counter.ChipCounter(screen, 455, 750)
    ai_chips1 = chip_counter.ChipCounter(screen, 100,200)
    ai_chips2 = chip_counter.ChipCounter(screen, 900,200)
    ai_chips3 = chip_counter.ChipCounter(screen, 1300,750)

    winner = None


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
            if event.type == pygame.KEYDOWN:
                players_chips.update(-2)
                player.bet(event.key)

        screen.fill((53, 101, 57))
        for ddd in cards_main_list:
            ddd.draw(game_round)

        screen.blit(poker_chip, (400,600))
        player.draw()
        screen.blit(poker_chip, (45,65))
        screen.blit(poker_chip, (845,65))
        screen.blit(poker_chip, (1250,600))



        ai0.draw()
        ai1.draw()
        ai2.draw()
        players_chips.draw()
        ai_chips1.draw()
        ai_chips2.draw()
        ai_chips3.draw()


        if game_round == 5:
            for player in players:
                player.hand_check(cards)

            break



        pygame.display.update()
if __name__ == "__main__":
    main()
