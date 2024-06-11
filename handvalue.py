import pygame
import card

# hand values and corresponding levels:
    #0 = high card
    #1 = pair
    #2 = two pair
    #3 = three of a kind
    #4 = straigh
    #5 = flush
    #6 = full house
    #7 = four of a kind
    #8 = straight flush


def hand_value(card1, card2, card3, card4, card5, card6, card7):
    card1_suite = card1[1]
    card2_suite = card2[1]
    card3_suite = card3[1]
    card4_suite = card4[1]
    card5_suite = card5[1]
    card6_suite = card6[1]
    card7_suite = card7[1]
    card1_value = card1[0]
    card2_value = card2[0]
    card3_value = card3[0]
    card4_value = card4[0]
    card5_value = card5[0]
    card6_value = card6[0]
    card7_value = card7[0]


