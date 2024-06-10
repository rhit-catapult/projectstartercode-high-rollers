import pygame
import random

suits = ["Hearts", "Clubs", "Diamonds", "Spades"]

for suit in suits:
    img_Kings = pygame.image.load("Cards/card" + suit + "K.png")
    img_Queens = pygame.image.load("Cards/card" + suit + "Q.png")
    img_Jacks = pygame.image.load("Cards/card" + suit + "J.png")
    img_Aces = pygame.image.load("Cards/card" + suit + "A.png")
    for i in range(2, 10):
        Numerical_Cards = pygame.image.load("Cards/card" + suit + str(i) + ".png")
