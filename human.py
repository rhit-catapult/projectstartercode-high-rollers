import pygame
import handvalue
import sys

class Human:
    def __init__(self, screen):
        self.screen = screen
        self.my_card_list = []
        self.x = 1000
        self.y = 600
        self.grad_hat = pygame.image.load("graduation-hat.png")
        self.image = pygame.transform.scale(self.grad_hat, (200, 120))
        self.chips = 100

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def hand_check(self, main_card_list):
        self.card = main_card_list[0]
        self.my_card_list.append(self.card)
        self.card = main_card_list[1]
        self.my_card_list.append(self.card)
        for k in range(8, 13):
            self.card = main_card_list[k]
            self.my_card_list.append(self.card)

        hand = handvalue.Hand()
        hand.set_cards(self.my_card_list)
        self.my_hand = hand.hand_value()
        self.hand_level = self.my_hand[0]
        self.high_card = self.my_hand[1]

    def bet(self, key):
        print(key)
        if key == pygame.K_a:

        if key == pygame.K_s:

        if key == pygame.K_d:

        if key == pygame.K_f