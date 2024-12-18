import unittest
from unittest import TestCase
from Card import Card

class TestCard(unittest.TestCase):
    def test_card_initialization_valid(self):
        """Test valid card initialization."""
        card = Card(14, 4)  # Ace of Spades
        self.assertEqual(card.value, 14)
        self.assertEqual(card.suit, 4)

    def test_card_initialization_invalid_value(self):
        """Test card initialization with an invalid value."""
        with self.assertRaises(ValueError):
            Card(1, 3)  # Invalid value (must be between 2 and 14)

    def test_card_initialization_invalid_suit(self):
        """Test card initialization with an invalid suit."""
        with self.assertRaises(ValueError):
            Card(10, 5)  # Invalid suit (must be between 1 and 4)

    def test_card_str(self):
        """Test the string representation of cards."""
        card1 = Card(14, 1)  # Ace of Hearts
        card2 = Card(11, 3)  # Jack of Clubs
        card3 = Card(2, 2)   # Two of Diamonds

        self.assertEqual(str(card1), "Ace of Hearts")
        self.assertEqual(str(card2), "Jack of Clubs")
        self.assertEqual(str(card3), "Two of Diamonds")

    def test_card_equality(self):
        """Test the equality operator (__eq__)."""
        card1 = Card(10, 2)
        card2 = Card(10, 2)
        card3 = Card(10, 3)

        self.assertEqual(card1, card2)
        self.assertNotEqual(card1, card3)

    def test_card_greater_than(self):
        """Test the greater than operator (__gt__)."""
        card1 = Card(10, 3)  # Ten of Clubs
        card2 = Card(9, 4)   # Nine of Spades
        card3 = Card(10, 2)  # Ten of Diamonds (lower suit than card1)

        self.assertTrue(card1 > card2)  # Compare by value
        self.assertTrue(card1 > card3)  # Compare by suit when values are equal
        self.assertFalse(card3 > card1)

    def test_card_repr(self):
        """Test the developer-friendly representation (__repr__)."""
        card = Card(14, 4)
        self.assertEqual(repr(card), "Card(14, '4')")

if __name__ == "__main__":
    unittest.main()
