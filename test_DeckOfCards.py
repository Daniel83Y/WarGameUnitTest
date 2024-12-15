import unittest
from unittest import TestCase
from unittest.mock import patch, MagicMock
from DeckOfCards import DeckOfCards
from Card import Card

class TestDeckOfCards(TestCase):
    def setUp(self):
        # Set up a fresh DeckOfCards instance before each test.
        self.deck = DeckOfCards()

    def tearDown(self):
        # Clean up resources or reset any state after each test.
        del self.deck  # Explicitly delete the deck instance (optional in Python).

    # Initialization Tests
    def test_initialization_card_count(self):
        # Test that the deck contains exactly 52 cards upon initialization.
        self.assertEqual(len(self.deck.cards), 52)

    def test_initialization_unique_cards(self):
        # Test that all cards in the deck are unique upon initialization.
        card_set = set(str(card) for card in self.deck.cards)
        self.assertEqual(len(card_set), 52)

    def test_initialization_correct_values_and_suits(self):
        # Test that the deck contains the correct combinations of values and suits.
        suits = ['Diamond', 'Spade', 'Heart', 'Club']
        values = range(1, 14)
        values_dict = {
            1: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
            11: "Jack", 12: "Queen", 13: "King"
        }

        # Expected card strings.
        expected_cards = {
            f"{values_dict[value]} of {suit}" for suit in suits for value in values
        }

        # Actual card strings from the deck.
        actual_cards = {str(card) for card in self.deck.cards}

        # Assert the sets match.
        self.assertEqual(expected_cards, actual_cards)

    # __str__ Tests
    def test_str_returns_string(self):
        # Test that the string representation of the deck is a string.
        self.assertTrue(isinstance(str(self.deck), str))

    def test_str_contains_card_example(self):
        # Test that the string representation contains a specific card.
        self.assertIn("Ace of Diamond", str(self.deck))

    def test_str_empty_deck(self):
        # Test that an empty deck has an empty string representation.
        for _ in range(52):
            self.deck.deal_one()
        self.assertEqual(str(self.deck), "")

    def test_str_matches_card_order(self):
        # Test that the string representation matches the current card order.
        expected_str = ", ".join(str(card) for card in self.deck.cards)
        self.assertEqual(str(self.deck), expected_str)

    # Shuffle Tests
    @patch("DeckOfCards.DeckOfCards.shuffle")
    def test_shuffle_function_called(self, mock_shuffle):
        # Test that the shuffle method is called.
        self.deck.shuffle()
        mock_shuffle.assert_called_once()

    def test_shuffle_changes_order(self):
        # Test that the shuffle method changes the order of cards.
        original_order = list(self.deck.cards)
        self.deck.shuffle()
        self.assertNotEqual(self.deck.cards, original_order)

    def test_shuffle_preserves_card_count(self):
        # Test that the shuffle method does not change the number of cards.
        self.deck.shuffle()
        self.assertEqual(len(self.deck.cards), 52)

    def test_shuffle_no_duplicates(self):
        # Test that the shuffle method does not introduce duplicate cards.
        self.deck.shuffle()
        card_set = set(str(card) for card in self.deck.cards)
        self.assertEqual(len(card_set), 52)

    # deal_one Tests
    @patch("DeckOfCards.DeckOfCards.deal_one", return_value=Card(1, "Diamond"))
    def test_deal_one_mocked_card_value(self, mock_deal_one):
        # Test that deal_one returns a mocked card with the correct value.
        card = self.deck.deal_one()
        self.assertEqual(card.value, 1)

    @patch("DeckOfCards.DeckOfCards.deal_one", return_value=Card(1, "Diamond"))
    def test_deal_one_mocked_card_suit(self, mock_deal_one):
        # Test that deal_one returns a mocked card with the correct suit.
        card = self.deck.deal_one()
        self.assertEqual(card.suit, "Diamond")

    def test_deal_one_reduces_size(self):
        # Test that deal_one reduces the number of cards in the deck.
        initial_size = len(self.deck.cards)
        self.deck.deal_one()
        self.assertEqual(len(self.deck.cards), initial_size - 1)

    def test_deal_one_no_duplicates(self):
        # Test that deal_one removes the dealt card from the deck.
        dealt_cards = set()
        for _ in range(52):
            card = self.deck.deal_one()
            self.assertNotIn(str(card), dealt_cards)
            dealt_cards.add(str(card))

    def test_deal_one_empty_deck_error(self):
        # Test that deal_one raises a ValueError when the deck is empty.
        for _ in range(52):
            self.deck.deal_one()
        with self.assertRaises(ValueError):
            self.deck.deal_one()

    # reset_deck Tests
    @patch("DeckOfCards.DeckOfCards.reset_deck")
    def test_reset_deck_function_called(self, mock_reset_deck):
        # Test that the reset_deck method is called.
        self.deck.reset_deck()
        mock_reset_deck.assert_called_once()

    def test_reset_deck_restores_card_count(self):
        # Test that reset_deck restores the deck to its original size.
        self.deck.shuffle()
        self.deck.deal_one()
        self.deck.reset_deck()
        self.assertEqual(len(self.deck.cards), 52)

    def test_reset_deck_restores_unique_cards(self):
        # Test that reset_deck restores all unique cards to the deck.
        self.deck.shuffle()
        self.deck.deal_one()
        self.deck.reset_deck()
        card_set = set(str(card) for card in self.deck.cards)
        self.assertEqual(len(card_set), 52)

if __name__ == "__main__":
    unittest.main()
