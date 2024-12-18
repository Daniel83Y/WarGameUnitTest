from DeckOfCards import DeckOfCards
from Player import Player

class CardGame:
    def __init__(self, player1_name, player2_name, cards_per_player=26):
        if not isinstance(player1_name, str):
            raise TypeError('player1_name must be a string')
        if not isinstance(player2_name, str):
            raise TypeError('player2_name must be a string')
        if not isinstance(cards_per_player, int):
            raise TypeError('cards_per_player must be an integer')
        if not (10 <= cards_per_player <= 26):
            raise ValueError('cards_per_player must be between 10 and 26')

        self.cards_per_player = cards_per_player
        self.deck = DeckOfCards()
        self.player1 = Player(player1_name, cards_per_player)
        self.player2 = Player(player2_name, cards_per_player)
        self.game_started = False  # Flag to prevent restarting the game

        self.new_game()

    def new_game(self, force_reset=False):
        """
        Initialize a new game if it hasn't already started.
        If force_reset is True, allow resetting the game (for testing purposes).
        """
        if self.game_started and not force_reset:
            print("⚠️ The game has already started. You cannot start again.")
            return  # Prevent re-initialization unless forced

        self.deck = DeckOfCards()  # Reset the deck
        self.deck.shuffle()
        self.player1.set_hand(self.deck)
        self.player2.set_hand(self.deck)
        self.game_started = True  # Set the flag to True
        print("🎴 A new game has been initialized!")

    def get_winner(self):
        if len(self.player1.deck_of_cards) > len(self.player2.deck_of_cards):
            return self.player1
        elif len(self.player1.deck_of_cards) < len(self.player2.deck_of_cards):
            return self.player2
        else:
            return None
