class Card:
    def __init__(self, value, suit):
        # Initializes a Card object with a value and a suit.
        # Validates that the value and suit are within valid ranges.
        if value < 2 or value > 14:
            raise ValueError("Value must be between 2 and 14.")
        self.value = value
        if suit <1 or suit >4:
            raise ValueError("Suits must be between 1 and 4")
        self.suit = suit

    def __str__(self):
        # User-friendly string representation of the card.
        values_dict = {
            2: "Two", 3: "Three", 4: "Four", 5: "Five",
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
            11: "Jack", 12: "Queen", 13: "King", 14: "Ace"
        }

        suits_dict = {
            1: "Hearts", 2: "Diamonds", 3: "Clubs", 4: "Spades"
        }

        value_str = values_dict.get(self.value, "Unknown")
        suit_str = suits_dict.get(self.suit, "Unknown")

        return f"{value_str} of {suit_str}"

    def __repr__(self):
        # Developer-friendly representation of the card.
        return f"Card({self.value}, '{self.suit}')"

    def __gt__(self, other):
        """Compare if this card is greater than another card."""
        if not isinstance(other, Card):
            raise ValueError("Cannot compare a Card with a non-Card object.")
        if self.value == other.value:
            return self.suit > other.suit
        return self.value > other.value

    def __eq__(self, other):
        """Check if this card is equal to another card."""
        if not isinstance(other, Card):
            raise ValueError("Cannot compare a Card with a non-Card object.")
        return self.value == other.value and self.suit == other.suit
