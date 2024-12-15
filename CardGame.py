from DeckOfCards import DeckOfCards
from Player import Player

class CardGame:
    def __init__(self, player1_name, player2_name, cards_per_player=26):
        if cards_per_player > 26 or cards_per_player < 10:
            raise ValueError("Number of cards per player must be between 10 and 26.")
        self.deck = DeckOfCards()
        self.deck.shuffle()
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        for _ in range(cards_per_player):
            self.player1.add_card(self.deck.deal_one())
            self.player2.add_card(self.deck.deal_one())

    def new_game(self):
        self.deck = DeckOfCards()
        self.deck.shuffle()
        self.player1.set_hand([])
        self.player2.set_hand([])
        for _ in range(26):
            self.player1.add_card(self.deck.deal_one())
            self.player2.add_card(self.deck.deal_one())

    def get_winner(self):
        if len(self.player1.hand) > len(self.player2.hand):
            return self.player1.name
        elif len(self.player1.hand) < len(self.player2.hand):
            return self.player2.name
        else:
            return None
