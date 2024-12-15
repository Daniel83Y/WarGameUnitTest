import unittest
from unittest import TestCase
from unittest.mock import patch
from CardGame import CardGame
from Player import Player
from Card import Card


class TestCardGame(TestCase):
    def setUp(self):
        # Set up common objects and mocks for tests
        self.player1_name = "Alice"
        self.player2_name = "Bob"
        self.cards_per_player = 26

        # Create a mock for DeckOfCards
        self.mock_deck_patcher = patch('CardGame.DeckOfCards')  # Patch DeckOfCards in CardGame
        self.mock_deck = self.mock_deck_patcher.start()
        self.mock_deck_instance = self.mock_deck.return_value  # Mock instance of DeckOfCards

        # Configure the mock to return Card objects
        self.mock_deck_instance.deal_one.side_effect = self.create_card_list(52)

        # Initialize the game
        self.game = CardGame(self.player1_name, self.player2_name, self.cards_per_player)

    def tearDown(self):
        # Stop all patches after each test
        self.mock_deck_patcher.stop()

    @staticmethod
    def create_card_list(count):
        """
        Helper method to create a list of Card objects for testing.
        :param count: Number of cards to generate.
        :return: List of Card objects.
        """
        return [Card(value=(i % 13) + 1, suit="Diamond") for i in range(count)]

    # Initialization Tests
    def test_initialization_player1_name(self):
        self.assertEqual(self.game.player1.name, self.player1_name)

    def test_initialization_player2_name(self):
        self.assertEqual(self.game.player2.name, self.player2_name)

    def test_initialization_deck_is_shuffled(self):
        self.mock_deck_instance.shuffle.assert_called_once()

    def test_initialization_player1_hand_size(self):
        self.assertEqual(len(self.game.player1.hand), self.cards_per_player)

    def test_initialization_player2_hand_size(self):
        self.assertEqual(len(self.game.player2.hand), self.cards_per_player)

    def test_initialization_invalid_cards_per_player_low(self):
        with self.assertRaises(ValueError):
            CardGame(self.player1_name, self.player2_name, cards_per_player=9)

    def test_initialization_invalid_cards_per_player_high(self):
        with self.assertRaises(ValueError):
            CardGame(self.player1_name, self.player2_name, cards_per_player=27)

    # New Game Tests
    def test_new_game_resets_deck_and_shuffles(self):
        # Reset side_effect before calling new_game
        self.mock_deck_instance.deal_one.side_effect = self.create_card_list(52)
        self.game.new_game()
        self.mock_deck_instance.shuffle.assert_called()

    def test_new_game_player1_hand_size(self):
        # Reset side_effect before calling new_game
        self.mock_deck_instance.deal_one.side_effect = self.create_card_list(52)
        self.game.new_game()
        self.assertEqual(len(self.game.player1.hand), self.cards_per_player)

    def test_new_game_player2_hand_size(self):
        # Reset side_effect before calling new_game
        self.mock_deck_instance.deal_one.side_effect = self.create_card_list(52)
        self.game.new_game()
        self.assertEqual(len(self.game.player2.hand), self.cards_per_player)

    # Get Winner Tests
    def test_get_winner_player1(self):
        self.game.player1 = Player(self.player1_name, hand=self.create_card_list(30))
        self.game.player2 = Player(self.player2_name, hand=self.create_card_list(20))
        self.assertEqual(self.game.get_winner(), self.player1_name)

    def test_get_winner_player2(self):
        self.game.player1 = Player(self.player1_name, hand=self.create_card_list(20))
        self.game.player2 = Player(self.player2_name, hand=self.create_card_list(30))
        self.assertEqual(self.game.get_winner(), self.player2_name)

    def test_get_winner_tie(self):
        self.game.player1 = Player(self.player1_name, hand=self.create_card_list(self.cards_per_player))
        self.game.player2 = Player(self.player2_name, hand=self.create_card_list(self.cards_per_player))
        self.assertIsNone(self.game.get_winner())


if __name__ == "__main__":
    unittest.main()
