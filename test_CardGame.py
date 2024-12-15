import unittest
from CardGame import CardGame
from Card import Card


class TestCardGame(unittest.TestCase):
    def setUp(self):
        # Initialize a new game with mocked players
        self.player1_name = "Alice"
        self.player2_name = "Bob"
        self.cards_per_player = 26
        self.game = CardGame(self.player1_name, self.player2_name, self.cards_per_player)

    def test_initialization(self):
        # Test if the game initializes correctly
        self.assertEqual(self.game.player1.name, self.player1_name)
        self.assertEqual(self.game.player2.name, self.player2_name)
        self.assertEqual(len(self.game.player1.hand), self.cards_per_player)
        self.assertEqual(len(self.game.player2.hand), self.cards_per_player)

    def test_new_game(self):
        # Test if new_game properly resets the game
        self.game.new_game()
        self.assertEqual(len(self.game.player1.hand), 26)
        self.assertEqual(len(self.game.player2.hand), 26)

    def test_get_winner_player1_wins(self):
        # Test get_winner when Player 1 wins
        self.game.player1.set_hand([Card(1, "Diamond")] * 30)
        self.game.player2.set_hand([Card(1, "Spade")] * 20)
        self.assertEqual(self.game.get_winner(), self.player1_name)

    def test_get_winner_player2_wins(self):
        # Test get_winner when Player 2 wins
        self.game.player1.set_hand([Card(1, "Diamond")] * 20)
        self.game.player2.set_hand([Card(1, "Spade")] * 30)
        self.assertEqual(self.game.get_winner(), self.player2_name)

    def test_get_winner_tie(self):
        # Test get_winner when it's a tie
        self.game.player1.set_hand([Card(1, "Diamond")] * 26)
        self.game.player2.set_hand([Card(1, "Spade")] * 26)
        self.assertIsNone(self.game.get_winner())

    def test_invalid_cards_per_player(self):
        # Test if ValueError is raised for invalid cards_per_player values
        with self.assertRaises(ValueError):
            CardGame(self.player1_name, self.player2_name, cards_per_player=9)  # Too few cards
        with self.assertRaises(ValueError):
            CardGame(self.player1_name, self.player2_name, cards_per_player=27)  # Too many cards

    def test_new_game_resets_hands(self):
        # Remove cards from players' hands before calling new_game
        self.game.player1.set_hand([Card(1, "Diamond")])
        self.game.player2.set_hand([Card(2, "Spade")])

        # Call new_game and verify hands are reset
        self.game.new_game()
        self.assertEqual(len(self.game.player1.hand), 26)
        self.assertEqual(len(self.game.player2.hand), 26)
        self.assertNotEqual(self.game.player1.hand, [Card(1, "Diamond")])
        self.assertNotEqual(self.game.player2.hand, [Card(2, "Spade")])


if __name__ == "__main__":
    unittest.main()
