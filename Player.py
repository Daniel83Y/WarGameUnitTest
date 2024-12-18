from Card import Card
import random
from DeckOfCards import DeckOfCards


class Player:
    def __init__(self, name, card_amount=26):
        if not isinstance(card_amount, int):
            raise TypeError('card_amount must be an integer')
        if not isinstance(name, str):
            raise TypeError('name must be a string')
        # Initialize Player with a name and a number of cards
        self.name = name
        if not (10 <= card_amount <= 26):
            card_amount = 26
        self.card_amount = card_amount
        self.deck_of_cards = []

    def __str__(self):
        # Return a string showing the player's name and their hand of cards.
        hand_str = ", ".join(str(card) for card in self.deck_of_cards)
        return f"Player: {self.name}, Hand: {hand_str if hand_str else 'No Cards'}"

    def add_card(self, card):
        # Add a Card object to the player's hand.
        # Raise ValueError if the input is not a Card.
        if not isinstance(card, Card):
            raise ValueError("Only Card objects can be added to the hand.")
        self.deck_of_cards.append(card)

    def get_card(self):
        if not self.deck_of_cards:
            raise IndexError(f"{self.name} has no cards to remove.")
        card = random.choice(self.deck_of_cards)
        self.deck_of_cards.remove(card)
        return card

    def set_hand(self, cards):
        # Replace the player's hand with cards dealt from a DeckOfCards object
        if not isinstance(cards, DeckOfCards):
            raise TypeError('cards must be a DeckOfCards object')

        self.deck_of_cards = [cards.deal_one() for _ in range(self.card_amount)]

