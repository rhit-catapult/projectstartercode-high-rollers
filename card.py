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


def randomcard():
    suites = ['hearts', 'diamonds', 'clubs', 'spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suite = suites.pop(random.randint(0,3))
    value = values.pop(random.randint(0,12))
    card = [value, suite]

    return card


def cardlist():
    pygame.init()
    cards = []
    while len(cards) < 13:
        randcard = randomcard()
        while not randcard in cards:
            cards.append(randcard)

    print(cards)


def main():





















