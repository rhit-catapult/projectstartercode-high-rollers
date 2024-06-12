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
class Hand:
    def __init__(self):
        self.level = 0
        self.hand_cards = []
    def set_cards(self, card_list):
        self.hand_cards = card_list
        self.level = 0


    def hand_value(self):
        suites = []
        values = []
        index = [0, 1, 2, 3, 4, 5, 6]
        self.highest_card = 0

        for card in self.hand_cards:
            suites.append(card[1])
            values.append(card[0])
        print(suites)
        print(values)
        self.high_card(values)
        pair = self.is_pair(values, index)
        if pair != 0:
            level = pair
        three_ofa_kind = self.is_3(values, index)
        if three_ofa_kind != 0:
            level = three_ofa_kind
        straight = self.is_straight(values)
        if straight != 0:
            level = straight
        flush = self.is_flush()
        if flush != 0:
            level = flush
        full_house = self.is_full_house(values)
        if full_house != 0:
            level = full_house
        four_kind = self.is_4(values)
        if four_kind != 0:
            level = four_kind
        straight_flush = self.is_straight_flush()
        if straight_flush != 0:
            level = straight_flush

        print(level)
        print(self.highest_card)
    def high_card(self, values):
        values_int = []
        for k in range(len(values)):
            value = values[k]
            value_int = value_index[value]
            values_int.append(value_int)
        values_int.sort(reverse=True)
        self.highest_card = values_int[0]
        self.level = 0

    def is_pair(self, values, index):
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
                                value = values[k]
                                value_int = value_index[value]
                                if value_int > self.highest_card:
                                    self.highest_card = value_int
                            if level == 0:
                                level = 1
                                value = values[k]
                                value_int = value_index[value]
                                self.highest_card = value_int
        return level
    def is_3(self, values, index):
        level = 0
        for k in range(len(values)):
            for h in range(len(values)):
                for l in range(len(values)):
                    p = index[h]
                    q = index[l]
                    if not l == h and not h == k and not l == k:
                        if values[k] == values[p] == values[q]:
                            level = 3
                            value = values[k]
                            value_int = value_index[value]
                            self.highest_card = value_int
        return level
    def is_straight(self, values):
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
                    value = values[top_card]
                    value_int = value_index[value]
                    self.highest_card = value_int
                    return level

            else:
                top_card = k
                straight_length = 1
        return 0
    def is_flush(self):
        values_int = []
        hearts = []
        diamonds = []
        spades = []
        clubs = []

        for card in self.hand_cards:
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
                values_int = []
                for k in range(len(suite)):
                    card = suite[k]
                    value = card[0]
                    value_int = value_index[value]
                    values_int.append(value_int)
                values_int.sort(reverse=True)
                level = 5
                self.highest_card = values_int[0]
                return level
        return 0


        # full house


        # straight flush
    def is_full_house(self, values):
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
                    self.highest_card = values_int[k-1]
                else:
                    pair = True
            k += 1

        if three_kind == True and pair == True:
            level = 6

        return level
    def is_4(self, values):
        values_int = []
        for k in range(len(values)):
            value = values[k]
            value_int = value_index[value]
            values_int.append(value_int)
        values_int.sort(reverse=True)

        for k in range(1, len(values)-3):
            if values_int[k] == values_int[k-1] == values_int[k+1] == values_int[k+2]:
                self.highest_card = values_int[k]
                return 7
            else:
                pass
        return 0
    def is_straight_flush(self):
        hearts = []
        diamonds = []
        spades = []
        clubs = []
        level = 0

        for card in self.hand_cards:
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
                straight = self.is_straight(values)
                if straight == 4:
                    level = 8
                elif straight == 0:
                    level = 0

        return level


hand=Hand()
hand.set_cards([["king", "diamonds"], ["king", "clubs"], ["king", "hearts"], ["4", "spades"], ["jack", "hearts"], ["jack", "diamonds"], ["10", "hearts"]])
hand.hand_value()