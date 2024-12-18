import unittest
from CardGame import CardGame
from Card import Card
from DeckOfCards import DeckOfCards
from Player import Player


class TestCardGame(unittest.TestCase):
    def setUp(self):
        # Initialize a new game
        self.player1_name = "Alice"
        self.player2_name = "Bob"
        self.cards_per_player = 26
        self.game = CardGame(self.player1_name, self.player2_name, self.cards_per_player)

    def test_initialization(self):
        """Test if the game initializes correctly."""
        self.assertEqual(self.game.player1.name, self.player1_name)
        self.assertEqual(self.game.player2.name, self.player2_name)
        self.assertEqual(len(self.game.player1.deck_of_cards), self.cards_per_player)
        self.assertEqual(len(self.game.player2.deck_of_cards), self.cards_per_player)

    def test_new_game(self):
        """Test if new_game properly resets the game."""
        # Shuffle and reset hands
        self.game.new_game()
        self.assertEqual(len(self.game.player1.deck_of_cards), 26)
        self.assertEqual(len(self.game.player2.deck_of_cards), 26)

    def test_get_winner_player1_wins(self):
        """Test get_winner when Player 1 has more cards."""
        # Mock Player 1 with more cards
        self.game.player1.deck_of_cards = [Card(14, 1)] * 30
        self.game.player2.deck_of_cards = [Card(13, 2)] * 20
        self.assertEqual(self.game.get_winner(), self.game.player1)

    def test_get_winner_player2_wins(self):
        """Test get_winner when Player 2 has more cards."""
        # Mock Player 2 with more cards
        self.game.player1.deck_of_cards = [Card(14, 1)] * 20
        self.game.player2.deck_of_cards = [Card(13, 2)] * 30
        self.assertEqual(self.game.get_winner(), self.game.player2)

    def test_get_winner_tie(self):
        """Test get_winner when both players have the same number of cards."""
        self.game.player1.deck_of_cards = [Card(14, 1)] * 26
        self.game.player2.deck_of_cards = [Card(13, 2)] * 26
        self.assertIsNone(self.game.get_winner())

    def test_invalid_cards_per_player(self):
        """Test if ValueError is raised for invalid cards_per_player values."""
        with self.assertRaises(ValueError):
            CardGame(self.player1_name, self.player2_name, cards_per_player=9)  # Too few cards
        with self.assertRaises(ValueError):
            CardGame(self.player1_name, self.player2_name, cards_per_player=27)  # Too many cards

    def test_new_game_resets_hands(self):
        """Test if new_game properly resets hands."""
        # Modify player hands before calling new_game
        self.game.player1.deck_of_cards = [Card(14, 1)]  # 1 card for Player 1
        self.game.player2.deck_of_cards = [Card(13, 2)]  # 1 card for Player 2

        # Call new_game with force_reset to simulate a fresh start
        self.game.new_game(force_reset=True)

        # Verify hands are reset
        self.assertEqual(len(self.game.player1.deck_of_cards), 26)
        self.assertEqual(len(self.game.player2.deck_of_cards), 26)
        self.assertNotEqual(self.game.player1.deck_of_cards, [Card(14, 1)])
        self.assertNotEqual(self.game.player2.deck_of_cards, [Card(13, 2)])


if __name__ == "__main__":
    unittest.main()