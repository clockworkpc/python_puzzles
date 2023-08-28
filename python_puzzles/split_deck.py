"""Split Deck Puzzle"""

import random
from python_puzzles import generate_deck


class Deck:
    def __init__(self):
        self.my_deck = generate_deck.main()

    def shuffle_deck(self):
        random.shuffle(self.cards())

    def cut_deck(self):
        middle = int(len(self.cards()) / 2)
        half1 = self.cards()[:middle]
        half2 = self.cards()[middle:]
        return {"half1": half1, "half2": half2}

    def count_cards_by_colour(self, cards, colour):
        result = [card for card in cards if card["colour"] == colour]
        return len(result)

    def cards(self):
        return self.my_deck["cards"]

    def find_cards(self, suit=None, colour=None):
        if not (suit or colour):
            return None

        key = "suit" if suit else "colour"
        value = suit or colour

        return [card for card in self.cards() if card[key] == value]

    def spades(self):
        return self.find_cards(suit="spades")

    def hearts(self):
        return self.find_cards(suit="hearts")

    def diamonds(self):
        return self.find_cards(suit="diamonds")

    def clubs(self):
        return self.find_cards(suit="clubs")

    def blacks(self):
        return self.find_cards(None, colour="black")

    def reds(self):
        result = self.find_cards(None, colour="red")
        return result
