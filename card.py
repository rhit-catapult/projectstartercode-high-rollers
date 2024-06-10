import pygame
import random
import sys
import time

suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
carddict = {}

carddict.update({"diamonds" : {"2": "cardDiamonds2.png",
                                "3": "cardDiamonds3.png",
                                "4": "cardDiamonds4.png",
                                "5": "cardDiamonds5.png",
                                "6": "cardDiamonds6.png",
                                "7": "cardDiamonds7.png",
                                "8": "cardDiamonds8.png",
                               "9": "cardDiamonds9.png",
                                "10": "cardDiamonds10.png",
                                "jack": "cardDiamondsJ.png",
                                "queen": "cardDiamondsQ.png",
                                "king": "cardDiamondsK.png",
                                "ace": "cardDiamondsA.png"},
                "spades" : {"2": "cardSpades2.png",
                            "3": "cardSpades3.png",
                            "4": "cardSpades4.png",
                            "5": "cardSpades5.png",
                            "6": "cardSpades6.png",
                            "7" : "cardSpades7.png",
                            "8" : "cardSpades8.png",
                            "9": "cardSpades9.png",
                            "10": "cardSpades10.png",
                            "jack": "cardSpadesJ.png",
                            "queen": "cardSpadesQ.png",
                            "king": "cardSpadesK.png",
                            "ace": "cardSpadesA.png"},
                "clubs" : {"2": "cardClubs2.png",
                            "3": "cardClubs3.png",
                            "4": "cardClubs4.png",
                            "5": "cardClubs5.png",
                            "6": "cardClubs6.png",
                            "7": "cardClubs7.png",
                            "8": "cardClubs8.png",
                            "9": "cardClubs9.png",
                            "10": "cardClubs10.png",
                            "jack": "cardClubsJ.png",
                            "queen": "cardClubsQ.png",
                            "king": "cardClubsK.png",
                            "ace": "cardClubsA.png"},
                "hearts": {"2": "cardHearts2.png",
                            "3": "cardHearts3.png",
                            "4": "cardHearts4.png",
                            "5": "cardHearts5.png",
                            "6": "cardHearts6.png",
                            "7": "cardHearts7.png",
                            "8": "cardHearts8.png",
                            "9": "cardHearts9.png",
                            "10": "cardHearts10.png",
                            "jack": "cardHeartsJ.png",
                            "queen": "cardHeartsQ.png",
                            "king": "cardHeartsK.png",
                            "ace": "cardHeartsA.png"}})

def randomcard():
    suites = ['hearts', 'diamonds', 'clubs', 'spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suite = suites.pop(random.randint(0,3))
    value = values.pop(random.randint(0,12))
    card = [value, suite]

    return card

cards = []
def cardlist():
    pygame.init()
    while len(cards) < 13:
        randcard = randomcard()
        while not randcard in cards:
            cards.append(randcard)

class Card:
    def __init__(self, screen, cardnumber):
        self.screen = screen
        self.cardnumber = cardnumber
        self.card = cards.pop(cardnumber)
        self.suite = self.card.pop(1)
        self.value = self.card.pop(0)
        self.cardchoice = carddict[self.suite][self.value]
        self.img = pygame.image.load(f"Cards/{self.cardchoice}")
        self.back_img = pygame.image.load(f"Cards/cardBack_red4.png")
        self.face_up = False

    def draw():
        if self.face_up == True:
            self.screen.blit(self.img, (420, 340))
        else:
            self.screen.blit(self.back_img, (420, 340))

        while True:
            if event.type == pygame.KEYDOWN:
                    pressed_key = pygame.key.get_pressed()
                    if pressed_key[pygame.K_SPACE]:
                        face_up = True
            pygame.display.update()




















