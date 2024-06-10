import pygame
import sys
import random
import time

def randomcard():
    suites = ['hearts', 'diamonds', 'clubs', 'spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suite = suites.pop(random.randint(0,3))
    value = values.pop(random.randint(0,12))
    card = [value, suite]

    return card


def main():
    # turn on pygame
    pygame.init()
    cards = []
    while len(cards) < 13:
        randcard = randomcard()
        while not randcard in cards:
            cards.append(randcard)

    print(cards)


main()