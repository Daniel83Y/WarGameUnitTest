import unittest
from unittest import TestCase
from Card import Card
from Player import Player

class TestPlayer(TestCase):
    def setUp(self):
        self.card1 = Card(1, "Diamond")
        self.card2 = Card(2, "Heart")
        self.card3 = Card(3, "Club")
        self.card4 = Card(4, "Spade")
        self.card5 = Card(5, "Diamond")

        self.player_name = "Alice"
        self.mock_hand = [self.card1, self.card2, self.card3, self.card4, self.card5]
        self.player = Player(self.player_name, self.mock_hand)

    def test_initialization_name(self):
        self.assertEqual(self.player.name, self.player_name)

    def test_initialization_hand_length(self):
        self.assertEqual(len(self.player.hand), 5)

    def test_initialization_hand_first_card(self):
        self.assertEqual(self.player.hand[0], self.card1)

    def test_initialization_no_hand(self):
        empty_player = Player(self.player_name)
        self.assertEqual(len(empty_player.hand), 0)

    def test_initialization_invalid_hand(self):
        invalid_hand = ["not_a_card", 42, None]
        with self.assertRaises(ValueError):
            Player(self.player_name, invalid_hand)

    def test_add_card_length(self):
        new_card = Card(6, "Heart")
        self.player.add_card(new_card)
        self.assertEqual(len(self.player.hand), 6)

    def test_add_card_presence(self):
        new_card = Card(6, "Heart")
        self.player.add_card(new_card)
        self.assertIn(new_card, self.player.hand)

    def test_add_card_invalid(self):
        with self.assertRaises(ValueError):
            self.player.add_card("not_a_card")

    def test_get_card_return_value(self):
        self.assertEqual(self.player.get_card(0), self.card1)

    def test_get_card_removes_card(self):
        self.player.get_card(0)
        self.assertNotIn(self.card1, self.player.hand)

    def test_get_card_index_error(self):
        with self.assertRaises(IndexError):
            self.player.get_card(10)

    def test_get_card_empty_hand_error(self):
        empty_player = Player(self.player_name)
        with self.assertRaises(IndexError) as context:
            empty_player.get_card(0)
        self.assertEqual(str(context.exception), f"{self.player_name} has no cards to remove.")

    def test_set_hand_new_hand_length(self):
        new_hand = [Card(7, "Spade"), Card(8, "Club")]
        self.player.set_hand(new_hand)
        self.assertEqual(len(self.player.hand), 2)

    def test_set_hand_new_hand_cards(self):
        new_hand = [Card(7, "Spade"), Card(8, "Club")]
        self.player.set_hand(new_hand)
        self.assertEqual(self.player.hand, new_hand)

    def test_set_hand_empty_list(self):
        self.player.set_hand([])
        self.assertEqual(len(self.player.hand), 0)

    def test_set_hand_invalid_hand(self):
        invalid_hand = ["not_a_card", 42, None]
        with self.assertRaises(ValueError):
            self.player.set_hand(invalid_hand)

    def test_str_representation_with_cards(self):
        expected_str = f"Player: {self.player_name}, Hand: {self.card1}, {self.card2}, {self.card3}, {self.card4}, {self.card5}"
        self.assertEqual(str(self.player), expected_str)

    def test_str_representation_no_cards(self):
        empty_player = Player(self.player_name)
        expected_str = f"Player: {self.player_name}, Hand: No Cards"
        self.assertEqual(str(empty_player), expected_str)


if __name__ == "__main__":
    unittest.main()
