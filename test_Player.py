import unittest
from Card import Card
from Player import Player
from DeckOfCards import DeckOfCards


class TestPlayer(unittest.TestCase):
    def setUp(self):
        """Set up a Player instance and mock cards for testing."""
        self.card1 = Card(2, 1)  # Two of Hearts
        self.card2 = Card(3, 2)  # Three of Diamonds
        self.card3 = Card(4, 3)  # Four of Clubs
        self.card4 = Card(5, 4)  # Five of Spades
        self.card5 = Card(6, 1)  # Six of Hearts

        self.player_name = "Alice"
        self.player = Player(self.player_name, card_amount=5)

        # Manually add cards for tests
        self.player.add_card(self.card1)
        self.player.add_card(self.card2)
        self.player.add_card(self.card3)
        self.player.add_card(self.card4)
        self.player.add_card(self.card5)

    def test_initialization_name(self):
        """Test the player's name initialization."""
        self.assertEqual(self.player.name, self.player_name)

    def test_initialization_empty_hand(self):
        """Test that a player starts with an empty deck of cards."""
        new_player = Player("Bob")
        self.assertEqual(len(new_player.deck_of_cards), 0)

    def test_add_card_length(self):
        """Test that add_card adds a card to the hand."""
        new_card = Card(7, 2)  # Seven of Diamonds
        self.player.add_card(new_card)
        self.assertEqual(len(self.player.deck_of_cards), 6)

    def test_add_card_invalid(self):
        """Test that add_card raises a ValueError for invalid input."""
        with self.assertRaises(ValueError) as context:
            self.player.add_card("not_a_card")
        self.assertEqual(str(context.exception), "Only Card objects can be added to the hand.")

    def test_get_card_removes_card(self):
        """Test that get_card removes and returns a random card."""
        initial_length = len(self.player.deck_of_cards)
        card = self.player.get_card()
        self.assertIsInstance(card, Card)
        self.assertEqual(len(self.player.deck_of_cards), initial_length - 1)
        self.assertNotIn(card, self.player.deck_of_cards)

    def test_get_card_empty_hand_error(self):
        """Test that get_card raises an IndexError when the hand is empty."""
        empty_player = Player("Bob")
        with self.assertRaises(IndexError) as context:
            empty_player.get_card()
        self.assertEqual(str(context.exception), "Bob has no cards to remove.")

    def test_set_hand_valid_deck(self):
        """Test that set_hand properly sets a new hand from a DeckOfCards."""
        deck = DeckOfCards()
        self.player.set_hand(deck)
        self.assertEqual(len(self.player.deck_of_cards), self.player.card_amount)  # Expect 26 cards

    def test_set_hand_invalid_input(self):
        """Test that set_hand raises TypeError for invalid input."""
        with self.assertRaises(TypeError) as context:
            self.player.set_hand("not_a_deck")
        self.assertEqual(str(context.exception), "cards must be a DeckOfCards object")

    def test_str_representation(self):
        """Test the __str__ representation of the player."""
        expected_str = f"Player: {self.player_name}, Hand: Two of Hearts, Three of Diamonds, Four of Clubs, Five of Spades, Six of Hearts"
        self.assertEqual(str(self.player), expected_str)


if __name__ == "__main__":
    unittest.main()
