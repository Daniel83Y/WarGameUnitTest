import random
from Card import Card

class DeckOfCards:
    def __init__(self):
        suits = ['Diamond', 'Spade', 'Heart', 'Club']
        values = range(1, 14)
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_one(self):
        if not self.cards:
            raise ValueError("The deck is empty. No cards left to deal.")
        return self.cards.pop(0)

    def reset_deck(self):
        suits = ['Diamond', 'Spade', 'Heart', 'Club']
        values = range(1, 14)
        self.cards = [Card(value, suit) for suit in suits for value in values]
