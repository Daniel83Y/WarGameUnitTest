class Card:
    def __init__(self, value, suit):
        # Initializes a Card object with a value and a suit.
        # Validates that the value and suit are within valid ranges.
        if value < 1 or value > 13:
            raise ValueError("Value must be between 1 and 13.")
        if suit.lower() not in ('diamond', 'spade', 'heart', 'club'):
            raise ValueError("Suit must be 'Diamond', 'Spade', 'Heart', 'Club'.")
        self.value = value
        self.suit = suit.capitalize()

    def __str__(self):
        # User-friendly string representation of the card.
        values_dict = {
            1: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
            11: "Jack", 12: "Queen", 13: "King"
        }
        value_str = values_dict.get(self.value, str(self.value))
        return f"{value_str} of {self.suit}"

    def __repr__(self):
        # Developer-friendly representation of the card.
        return f"Card({self.value}, '{self.suit}')"

    def __gt__(self, other):
        # Compares if the card's value is greater than another card's value.
        if not isinstance(other, Card):
            return NotImplemented
        return self.value > other.value

    def __lt__(self, other):
        # Compares if the card's value is less than another card's value.
        if not isinstance(other, Card):
            return NotImplemented
        return self.value < other.value

    def __eq__(self, other):
        # Checks equality between two cards based on value and suit.
        if not isinstance(other, Card):
            return NotImplemented
        return self.value == other.value and self.suit == other.suit

    def __ge__(self, other):
        # Compares if the card's value is greater than or equal to another card's value.
        if not isinstance(other, Card):
            return NotImplemented
        return self.value >= other.value

    def __le__(self, other):
        # Compares if the card's value is less than or equal to another card's value.
        if not isinstance(other, Card):
            return NotImplemented
        return self.value <= other.value

    @property
    def rank(self):
        # Returns the rank of the card (e.g., 'Ace', 'King', '5').
        values_dict = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
        return values_dict.get(self.value, str(self.value))
