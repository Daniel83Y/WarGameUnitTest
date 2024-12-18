import unittest
from DeckOfCards import DeckOfCards
from Card import Card


class TestDeckOfCards(unittest.TestCase):
    def setUp(self):
        """Set up a fresh DeckOfCards instance before each test."""
        self.deck = DeckOfCards()

    # Initialization Tests
    def test_initialization_card_count(self):
        """Test that the deck contains exactly 52 cards upon initialization."""
        self.assertEqual(len(self.deck.cards), 52)

    def test_initialization_unique_cards(self):
        """Test that all cards in the deck are unique upon initialization."""
        card_set = {str(card) for card in self.deck.cards}
        self.assertEqual(len(card_set), 52)  # Ensure all cards are unique

    def test_initialization_correct_values_and_suits(self):
        """Test that the deck contains the correct range of values and suits."""
        values = range(2, 15)  # Values: 2 to 14
        suits = range(1, 5)    # Suits: 1 to 4
        expected_cards = {f"{Card(value, suit)}" for suit in suits for value in values}
        actual_cards = {str(card) for card in self.deck.cards}
        self.assertEqual(expected_cards, actual_cards)

    # Shuffle Tests
    def test_shuffle_changes_order(self):
        """Test that shuffle changes the order of the cards."""
        original_order = list(self.deck.cards)
        self.deck.shuffle()
        self.assertNotEqual(self.deck.cards, original_order)

    def test_shuffle_preserves_card_count(self):
        """Test that shuffle does not change the number of cards."""
        original_count = len(self.deck.cards)
        self.deck.shuffle()
        self.assertEqual(len(self.deck.cards), original_count)

    # Deal One Tests
    def test_deal_one_reduces_size(self):
        """Test that deal_one reduces the number of cards by one."""
        initial_size = len(self.deck.cards)
        self.deck.deal_one()
        self.assertEqual(len(self.deck.cards), initial_size - 1)

    def test_deal_one_returns_card(self):
        """Test that deal_one returns a valid Card object."""
        card = self.deck.deal_one()
        self.assertIsInstance(card, Card)

    def test_deal_one_empty_deck_error(self):
        """Test that deal_one raises an IndexError when the deck is empty."""
        for _ in range(52):  # Dealing all cards in the deck
            self.deck.deal_one()
        with self.assertRaises(IndexError) as context:
            self.deck.deal_one()  # Attempt to deal from an empty deck
        self.assertIn("has no cards to remove", str(context.exception))


if __name__ == "__main__":
    unittest.main()
