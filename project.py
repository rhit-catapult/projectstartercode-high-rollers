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
    pot = 0
    pay_amount = 0

    clock = pygame.time.Clock()
    player = human.Human(screen)
    ai0 = AI.AI(screen, 0)
    ai1 = AI.AI(screen, 1)
    ai2 = AI.AI(screen, 2)
    players_chips = chip_counter.ChipCounter(screen, 455, 750)
    ai_chips1 = chip_counter.ChipCounter(screen, 100,200)
    ai_chips2 = chip_counter.ChipCounter(screen, 900,200)
    ai_chips3 = chip_counter.ChipCounter(screen, 1300,750)
    turn = 3
    last_raise = -1
    last_round = 0
    game_round = -1
    pressed_key = []
    next_turn = 3

    cards_main_list = []

    while True:
        if game_round > last_round or game_round == -1:
            last_round = game_round
            turn = 3
            if game_round == -1:
                cards_main_list = []
                cards = card.cardlist()
                game_round = 0
                pay_amount = 0
                for k in range(13):
                    cards_main_list.append(card.Card(screen, k, cards))
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pressed_key = pygame.key.get_pressed()
                if event.key == pygame.K_SPACE:
                    turn += 1
                    if turn == 4:
                        turn = 0

                    print(turn)
        if turn == 3 and not player.my_bet == 3:
            if not next_turn == 0:
                if not last_raise == 3:
                    player.bet(pressed_key, pay_amount)
                    pot += player.into_pot
                    pay_amount += player.increase
                    next_turn = 0
                    if player.my_bet == 1:
                        last_raise = 3
                else:
                    game_round += 1
                    turn = 3

        if turn == 0 and not ai0.my_bet == 3:
            if not next_turn == 1:
                if not last_raise == 0:
                    ai0.hand_check(cards)
                    ai0.bet(pay_amount)
                    pot += ai0.into_pot
                    pay_amount += ai0.increase
                    next_turn = 1
                    if player.my_bet == 1:
                        last_raise = 0
                else:
                        game_round += 1
                        turn = 3
        if turn == 1 and not ai1.my_bet == 3:
            if not next_turn == 2:
                if not last_raise == 1:
                    ai1.hand_check(cards)
                    ai1.bet(pay_amount)
                    pot += ai1.into_pot
                    pay_amount += ai1.increase
                    next_turn = 2
                    if player.my_bet == 1:
                        last_raise = 1
                else:
                    game_round += 1

        if turn == 2 and not ai2.my_bet == 3:
            if not next_turn == 3:
                if not last_raise == 2:
                    ai2.hand_check(cards)
                    ai2.bet(pay_amount)
                    pot += ai2.into_pot
                    pay_amount += ai2.increase
                    next_turn = 3
                    if player.my_bet == 1:
                        last_raise = 2
                else:
                    game_round += 1

        if game_round == 5:
            player.hand_check(cards)
            ai1.hand_check(cards)
            ai2.hand_check(cards)
            ai0.hand_check(cards)
            hand3 = player.hand_level
            hand0 = ai0.hand_level
            hand1 = ai1.hand_level
            hand2 = ai2.hand_level

            if hand3 > hand0 and hand3 > hand1 and hand3 > hand2:
                player.chips += pot
            if hand0 > hand3 and hand0 > hand1 and hand0 > hand2:
                ai0.chips += pot
            if hand1 > hand0 and hand1 > hand3 and hand1 > hand2:
                ai1.chips += pot
            if hand2 > hand0 and hand2 > hand1 and hand2 > hand3:
                ai2.chips += pot



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
        players_chips.draw(player.chips)
        ai_chips1.draw(ai0.chips)
        ai_chips2.draw(ai1.chips)
        ai_chips3.draw(ai2.chips)

        pygame.display.update()

        if game_round == 5:
            pot = 0
            game_round = -1

if __name__ == "__main__":
    main()
