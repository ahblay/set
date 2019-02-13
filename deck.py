from random import shuffle
from card import Card
import itertools


class Deck:
    def __init__(self):
        self.deck = self.generate()
        self.play = []

    def generate(self):
        cards = []
        colors = ['red', 'green', 'purple']
        shapes = ['oval', 'squiggle', 'diamond']
        fills = ['empty', 'shaded', 'solid']
        quantities = ['1', '2', '3']
        for color in colors:
            for shape in shapes:
                for fill in fills:
                    for quantity in quantities:
                        card = Card(color, shape, quantity, fill)
                        cards.append(card)
        return cards

    def shuffle(self):
        shuffle(self.deck)

    def deal(self, num, locations):
        play = []
        i = 0
        for _ in range(num):
            try:
                card = self.deck.pop(0)
                card.location = locations[i]
                play.append(card)
                i += 1
            except IndexError:
                break
        self.play += play

    def remove(self, indices=None, cards=None):
        if indices and cards:
            raise Exception("Both indices and cards provided. TMI.")
        if indices:
            for index in indices:
                del self.play[index]
        if cards:
            for card in cards:
                self.play.remove(card)
        else:
            raise Exception("No indices or cards provided.")

    def redeal(self, locations):
        i = 0
        while len(self.play) < 12 and len(self.deck) > 0:
            self.deal(1, [locations[i]])
            i += 1

    def is_set(self, cards):
        if len(cards) != 3:
            return False
        color = []
        shape = []
        fill = []
        quantity = []
        for card in cards:
            color.append(card.color)
            shape.append(card.shape)
            fill.append(card.fill)
            quantity.append(card.quantity)
        if len(list(set(color))) == 2 or \
           len(list(set(shape))) == 2 or \
           len(list(set(fill))) == 2 or \
           len(list(set(quantity))) == 2:
            return False
        return True

    def count_sets(self):
        combos = itertools.combinations(self.play, 3)
        set_counter = 0
        for combo in combos:
            if self.is_set(combo):
                set_counter += 1
        return set_counter