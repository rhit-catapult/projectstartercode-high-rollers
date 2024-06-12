import pygame
import random
import sys
import time
import card
import handvalue

pygame.init()
screen = pygame.display.set_mode((1400, 800))
pygame.display.set_caption("Poker")
screen.fill((53, 101, 57))
clock = pygame.time.Clock()

image_size = (200, 200)
cowboy = pygame.image.load("cowboy_hat.png")
fedora = pygame.image.load("fedora.png")
grad_hat = pygame.image.load("graduation-hat.png")
tophat = pygame.image.load("tophat.png")
cowboy = pygame.transform.scale(cowboy, image_size)
fedora = pygame.transform.scale(fedora, (150, 150))
grad_hat = pygame.transform.scale(grad_hat, (200, 120))
tophat = pygame.transform.scale(tophat, (150, 120))

class AI:
    def __init__(self, screen, ai_number):
        self.screen = screen
        self.ai_number = ai_number

        if self.ai_number == 0:
            self.x = 0
            self.y = 590
            self.my_cards = [2, 3]
            self.image = fedora
        if self.ai_number == 1:
            self.x = 200
            self.y = -50
            self.my_cards = [4, 5]
            self.image = cowboy
        if self.ai_number == 2:
            self.x = 1230
            self.y = 50
            self.my_cards = [5, 6]
            self.image = tophat

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def bet(self):
        pass


    def hand_check(self, main_card_list):
        self.my_card_list = []
        for card in self.my_cards:
            self.my_card_list.append(main_card_list[card])
        print(self.my_card_list)