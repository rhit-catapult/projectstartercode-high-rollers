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
    suite = suites[random.randint(0,3)]
    value = values[random.randint(0,12)]
    card = [value, suite]

    return card


def cardlist():
    pygame.init()
    cards = []
    while len(cards) < 13:
        randcard = randomcard()
        while not randcard in cards:
            cards.append(randcard)
    return cards

class Card:
    def __init__(self, screen, cardnumber, cards):
        self.screen = screen
        self.cardnumber = cardnumber
        self.card = cards[self.cardnumber]
        self.suite = self.card[1]
        self.value = self.card[0]
        self.cardchoice = carddict[self.suite][self.value]
        self.img = pygame.image.load(f"Cards/{self.cardchoice}")
        self.back_img = pygame.image.load(f"Cards/cardBack_red4.png")

        if cardnumber == 0:
            self.x = 700
            self.y = 600
            self.face_up = True
        if cardnumber == 1:
            self.x = 550
            self.y = 600
            self.face_up = True
        if cardnumber == 2:
            self.x = 20
            self.y = 400
            self.back_img = pygame.transform.rotate(self.back_img, 270)
            self.img = pygame.transform.rotate(self.img, 270)
            self.face_up = False
        if cardnumber == 3:
            self.x = 20
            self.y = 250
            self.back_img = pygame.transform.rotate(self.back_img, 270)
            self.img = pygame.transform.rotate(self.img, 270)
            self.face_up = False
        if cardnumber == 4:
            self.x = 550
            self.y = 20
            self.face_up = False
        if cardnumber == 5:
            self.x = 700
            self.y = 20
            self.face_up = False
        if cardnumber == 6:
            self.x = 1200
            self.y = 250
            self.back_img = pygame.transform.rotate(self.back_img, 90)
            self.img = pygame.transform.rotate(self.img, 90)
            self.face_up = False
        if cardnumber == 7:
            self.x = 1200
            self.y = 400
            self.back_img = pygame.transform.rotate(self.back_img, 90)
            self.img = pygame.transform.rotate(self.img, 90)
            self.face_up = False
        if cardnumber == 8:
            self.x = 325
            self.y = 300
            self.face_up = False
        if cardnumber == 9:
            self.x = 475
            self.y = 300
            self.face_up = False
        if cardnumber == 10:
            self.x = 625
            self.y = 300
            self.face_up = False
        if cardnumber == 11:
            self.x = 775
            self.y = 300
            self.face_up = False
        if cardnumber == 12:
            self.x = 925
            self.y = 300
            self.face_up = False

    def draw(self, round):
        if round == 1:
            pass
        if round == 2:
            if 8 <= self.cardnumber <= 10:
                self.face_up = True
        if round == 3:
            if self.cardnumber == 11:
                self.face_up = True
        if round == 4:
            if self.cardnumber == 12:
                self.face_up = True
        if round == 5:
            if 2 <= self.cardnumber <= 7:
                self.face_up = True


        if self.face_up == True:
            self.screen.blit(self.img, (self.x, self.y))
        else:
            self.screen.blit(self.back_img, (self.x, self.y))




