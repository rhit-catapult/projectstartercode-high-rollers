import pygame
import random
import sys
import time

suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
carddict = {}

for suit in suits:
    img_Kings = pygame.image.load("Cards/card" + suit + "K.png")
    img_Queens = pygame.image.load("Cards/card" + suit + "Q.png")
    img_Jacks = pygame.image.load("Cards/card" + suit + "J.png")
    img_Aces = pygame.image.load("Cards/card" + suit + "A.png")
    for i in range(2, 10):
        Numerical_Cards = pygame.image.load("Cards/card" + suit + str(i) + ".png")

    carddict.update({suit : {"k" : img_Kings}})

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

def main():
    screen = pygame.display.set_mode((1400, 800))
    pygame.display.set_caption("Poker")
    screen.fill((53, 101, 57))
    cardlist()
    randcard = cards.pop(0)
    randsuite = randcard.pop(1)
    randvalue = randcard.pop(0)
    cardchoice = carddict[randsuite][randvalue]
    img = pygame.image.load(f"Cards/{cardchoice}")
    back_img = pygame.image.load(f"Cards/cardBack_red4.png")
    face_up = False



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                pressed_key = pygame.key.get_pressed()
                if pressed_key[pygame.K_SPACE]:
                    face_up = True

        if face_up == True:
            screen.blit(img, (420, 340))
        else:
            screen.blit(back_img, (420, 340))
        pygame.display.update()


if __name__ == "__main__":
    main()




















