import unittest
from unittest import TestCase
from Card import Card

class TestCard(TestCase):
    def setUp(self):
        # Set up common Card instances to be used in multiple tests.
        self.card_ace_diamond = Card(1, "Diamond")
        self.card_king_heart = Card(13, "Heart")
        self.card_five_club = Card(5, "Club")
        self.card_seven_diamond = Card(7, "Diamond")
        self.card_eight_spade = Card(8, "Spade")

    def test_card_initialization_value(self):
        # Test if the card value is initialized correctly.
        self.assertEqual(self.card_ace_diamond.value, 1)

    def test_card_initialization_suit(self):
        # Test if the card suit is initialized correctly.
        self.assertEqual(self.card_ace_diamond.suit, "Diamond")

    def test_card_invalid_value_low(self):
        # Test if a ValueError is raised for values below the valid range.
        with self.assertRaises(ValueError):
            Card(0, "Diamond")  # Value below range

    def test_card_invalid_value_high(self):
        # Test if a ValueError is raised for values above the valid range.
        with self.assertRaises(ValueError):
            Card(14, "Spade")  # Value above range

    def test_card_invalid_suit(self):
        # Test if a ValueError is raised for an invalid suit.
        with self.assertRaises(ValueError):
            Card(1, "InvalidSuit")

    def test_card_str_representation(self):
        # Test the string representation of the card.
        self.assertEqual(str(self.card_ace_diamond), "Ace of Diamond")

    def test_card_repr_representation(self):
        # Test the developer-friendly representation of the card.
        self.assertEqual(repr(self.card_king_heart), "Card(13, 'Heart')")

    def test_card_greater_than(self):
        # Test the greater than (>) comparison of two cards.
        card1 = Card(10, "Spade")
        card2 = Card(5, "Diamond")
        self.assertTrue(card1 > card2)

    def test_card_less_than(self):
        # Test the less than (<) comparison of two cards.
        card1 = Card(2, "Heart")
        card2 = Card(11, "Club")
        self.assertTrue(card1 < card2)

    def test_card_equality(self):
        # Test the equality (==) comparison of two cards with the same value and suit.
        card1 = Card(7, "Diamond")
        card2 = Card(7, "Diamond")
        self.assertTrue(card1 == card2)

    def test_card_inequality(self):
        # Test the inequality (!=) comparison of two cards with different values or suits.
        self.assertFalse(self.card_seven_diamond == self.card_eight_spade)

    def test_card_greater_than_or_equal_equal(self):
        # Test the greater than or equal to (>=) comparison for equal cards.
        card1 = Card(9, "Heart")
        card2 = Card(9, "Club")
        self.assertTrue(card1 >= card2)

    def test_card_greater_than_or_equal_greater(self):
        # Test the greater than or equal to (>=) comparison for a greater card.
        card1 = Card(10, "Heart")
        card2 = Card(9, "Club")
        self.assertTrue(card1 >= card2)

    def test_card_less_than_or_equal_equal(self):
        # Test the less than or equal to (<=) comparison for equal cards.
        card1 = Card(6, "Diamond")
        card2 = Card(6, "Club")
        self.assertTrue(card1 <= card2)

    def test_card_less_than_or_equal_less(self):
        # Test the less than or equal to (<=) comparison for a lesser card.
        card1 = Card(6, "Diamond")
        card2 = Card(7, "Club")
        self.assertTrue(card1 <= card2)

    def test_card_rank_ace(self):
        # Test the rank property for an Ace card.
        self.assertEqual(self.card_ace_diamond.rank, "Ace")

    def test_card_rank_king(self):
        # Test the rank property for a King card.
        self.assertEqual(self.card_king_heart.rank, "King")

    def test_card_rank_regular(self):
        # Test the rank property for a regular numbered card.
        self.assertEqual(self.card_five_club.rank, "5")

    def test_card_value_type(self):
        # Test if the card value is of type int.
        self.assertTrue(isinstance(self.card_five_club.value, int))

    def test_card_suit_type(self):
        # Test if the card suit is of type str.
        self.assertTrue(isinstance(self.card_five_club.suit, str))

    # Tests for invalid type comparisons
    def test_card_greater_than_invalid_type(self):
        # Test if TypeError is raised for greater than (>) comparison with an invalid type.
        with self.assertRaises(TypeError):
            _ = self.card_ace_diamond > 10

    def test_card_less_than_invalid_type(self):
        # Test if TypeError is raised for less than (<) comparison with an invalid type.
        with self.assertRaises(TypeError):
            _ = self.card_ace_diamond < "NotACard"

    def test_card_equality_invalid_type(self):
        # Test if equality (==) comparison with an invalid type returns False.
        self.assertFalse(self.card_ace_diamond == "NotACard")

    def test_card_greater_than_or_equal_invalid_type(self):
        # Test if TypeError is raised for greater than or equal to (>=) comparison with an invalid type.
        with self.assertRaises(TypeError):
            _ = self.card_ace_diamond >= []

    def test_card_less_than_or_equal_invalid_type(self):
        # Test if TypeError is raised for less than or equal to (<=) comparison with an invalid type.
        with self.assertRaises(TypeError):
            _ = self.card_ace_diamond <= {}

if __name__ == "__main__":
    unittest.main()
