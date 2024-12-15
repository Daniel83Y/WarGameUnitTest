from Card import Card


class Player:
    def __init__(self, name, hand=None):
        """
        Initializes a Player object with a name and an optional initial hand.

        :param name: The name of the player.
        :param hand: A list of Card objects to initialize the player's hand (default is empty).
        :raises ValueError: If any item in the provided list is not a Card object.
        """
        self.name = name
        if hand is None:
            self.hand = []  # Empty list of Card objects
        else:
            if not all(isinstance(card, Card) for card in hand):
                raise ValueError("All items in the hand must be Card objects.")
            self.hand = hand

    def __str__(self):
        """
        Returns a string representation of the player and their hand.

        :return: A string in the format "Player: [name], Hand: [cards]".
        """
        hand_str = ", ".join(str(card) for card in self.hand)
        return f"Player: {self.name}, Hand: {hand_str if hand_str else 'No Cards'}"

    def add_card(self, card):
        """
        Adds a card to the player's hand.
        :param card: A Card object to be added to the hand.
        :raises ValueError: If the provided object is not a Card.
        """
        if not isinstance(card, Card):
            raise ValueError("Only Card objects can be added to the hand.")
        self.hand.append(card)

    def get_card(self, index):
        """
        Removes the card from the player's hand at a specific index.

        :param index: The index of the card to remove.
        :return: The Card object removed from the hand.
        :raises IndexError: If the index is out of range or the hand is empty.
        """
        if not self.hand:
            raise IndexError(f"{self.name} has no cards to remove.")
        if index < 0 or index >= len(self.hand):
            raise IndexError(f"Invalid card index: {index}.")
        return self.hand.pop(index)  # Removes and returns the card at the given index

    def set_hand(self, cards):
        """
        Sets the player's hand to a new list of cards.

        :param cards: A list of Card objects to set as the player's hand.
        :raises ValueError: If any item in the provided list is not a Card object.
        """
        if not all(isinstance(card, Card) for card in cards):
            raise ValueError("All items in the hand must be Card objects.")
        self.hand = cards
