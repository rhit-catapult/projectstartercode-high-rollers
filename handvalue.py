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
    pair_card = -1

    for k in range(7):
        card_current = hand_cards[k]
        suites.append(card_current[1])
        values.append(card_current[0])
    print(suites)
    print(values)
    level = is_straight(values)
    #pair & 2 pair
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
                            pair_card = h


                else:
                    pass

    # 3 of a kind
    for k in range(len(values)):
        for h in range(len(values)):
            for l in range(len(values)):
                p = index[h]
                q = index[l]
                if not l == h and not h == k and not l == k:
                    if values[k] == values[p] == values[q]:
                        level = 3
                else:
                    pass

    # straight


    # flush
    for k in range(len(suites)):
        flush_number = 1
        for h in range(len(suites)):
            if not h == k:
                if suites[k] == suites[h]:
                    flush_number += 1
                    if flush_number == 5:
                        level = 5
            else:
                pass


    # full house


    # straight flush


    print(level)

def is_straight(values):
    values_int = []
    for k in range(len(values)):
        value = values[k]
        value_int = value_index[value]
        values_int.append(value_int)
    values_int.sort(reverse=True)
    val_int = copy.deepcopy(values_int)
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

hand_value(["7", "diamonds"], ["king", "clubs"], ["king", "hearts"], ["ace", "hearts"], ["queen", "hearts"], ["jack", "hearts"], ["10", "hearts"])