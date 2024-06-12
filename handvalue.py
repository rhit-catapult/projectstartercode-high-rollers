import pygame
import card
import copy

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


value_index = {}
value_index.update({"2": 2,
                    "3": 3,
                    "4": 4,
                    "5": 5,
                    "6": 6,
                    "7": 7,
                    "8": 8,
                    "9": 9,
                    "10": 10,
                    "jack": 11,
                    "queen": 12,
                    "king": 13,
                    "ace": 14})


def hand_value(card1, card2, card3, card4, card5, card6, card7):
    hand_cards = [card1, card2, card3, card4, card5, card6, card7]
    suites = []
    values = []
    level = 0
    index = [0, 1, 2, 3, 4, 5, 6]
    highest_card = 0

    for card in hand_cards:
        suites.append(card[1])
        values.append(card[0])
    print(suites)
    print(values)
    pair = is_pair(values, index)
    if pair != 0:
        level = pair
    three_ofa_kind = is_3(values, index)
    if three_ofa_kind != 0:
        level = three_ofa_kind
    straight = is_straight(values)
    if straight != 0:
        level = straight
    flush = is_flush(suites)
    if flush != 0:
        level = flush
    full_house = is_full_house(values)
    if full_house != 0:
        level = full_house
    four_kind = is_4(values)
    if four_kind != 0:
        level = four_kind
    straight_flush = is_straight_flush(hand_cards)
    if straight_flush != 0:
        level = straight_flush

    print(level)


def is_pair(values, index):
    pair_card = -1
    level = 0
    for k in range(len(values)):
        if not k == pair_card:
            for h in range(len(values)):
                if not h == k:
                    p = index[h]
                    if values[k] == values[p]:
                        if level == 1:
                            level = 2
                        if level == 0:
                            level = 1
    return level
def is_3(values, index):
    level = 0
    for k in range(len(values)):
        for h in range(len(values)):
            for l in range(len(values)):
                p = index[h]
                q = index[l]
                if not l == h and not h == k and not l == k:
                    if values[k] == values[p] == values[q]:
                        level = 3
    return level
def is_straight(values):
    values_int = []
    for k in range(len(values)):
        value = values[k]
        value_int = value_index[value]
        values_int.append(value_int)
    values_int.sort(reverse=True)
    k = 1
    while k < len(values_int):
        if values_int[k] == values_int[k - 1]:
            values_int.pop(k)
        else:
            k += 1
    straight_length = 1
    top_card = 0
    for k in range(1, len(values_int)):
        if values_int[k] == values_int[k - 1] - 1:
            straight_length += 1
            if straight_length == 5:
                level = 4
                return level

        else:
            top_card = k
            straight_length = 1
    return 0
def is_flush(suites):
    for k in range(len(suites)):
        flush_number = 1
        for h in range(len(suites)):
            if not h == k:
                if suites[k] == suites[h]:
                    flush_number += 1
                    if flush_number == 5:
                        level = 5
                        return level
    else:
        return 0


    # full house


    # straight flush
def is_full_house(values):
    values_int = []
    level = 0
    for k in range(len(values)):
        value = values[k]
        value_int = value_index[value]
        values_int.append(value_int)
    values_int.sort(reverse=True)
    three_kind = False
    pair = False
    k = 1
    while k < len(values_int):
        if values_int[k] == values_int[k-1]:
            if k < len(values_int)-1 and values_int[k+1] == values_int[k]:
                three_kind = True
                k += 1
            else:
                pair = True
        k += 1

    if three_kind == True and pair == True:
        level = 6

    return level
def is_4(values):
    values_int = []
    for k in range(len(values)):
        value = values[k]
        value_int = value_index[value]
        values_int.append(value_int)
    values_int.sort(reverse=True)

    for k in range(1, len(values)-3):
        if values_int[k] == values_int[k-1] == values_int[k+1] == values_int[k+2]:
            return 7
        else:
            pass
    return 0
def is_straight_flush(hand_cards):
    hearts = []
    diamonds = []
    spades = []
    clubs = []
    level = 0

    for card in hand_cards:
        if card[1] == "hearts":
            hearts.append(card)
        if card[1] == "diamonds":
            diamonds.append(card)
        if card[1] == "spades":
            spades.append(card)
        if card[1] == "clubs":
            clubs.append(card)

    suites = [hearts, diamonds, spades, clubs]

    for suite in suites:
        if len(suite) > 4:
            values = []
            for card in suite:
                values.append(card[0])
            straight = is_straight(values)
            if straight == 4:
                level = 8
            elif straight == 0:
                level = 0

    return level



hand_value(["king", "diamonds"], ["king", "clubs"], ["king", "hearts"], ["4", "spades"], ["queen", "hearts"], ["jack", "diamonds"], ["10", "hearts"])