from CardGame import CardGame

CARDS_AMOUNT = 26
GAME_ROUNDS = 10

class CardGameMain:
    def __init__(self):
        self.game = None
        self.turn_count = 0  # Initialize turn counter

    def start_game(self):
        """Start the card game with input validation and setup."""
        player1_name = input("Enter player 1 name: ").strip() or "Player 1"
        player2_name = input("Enter player 2 name: ").strip() or "Player 2"

        # Initialize the game
        self.game = CardGame(player1_name, player2_name, CARDS_AMOUNT)

        print("=" * 50)
        print("🎴 The Game has Started! 🎴")
        print(f"Players: {player1_name} vs {player2_name}")
        print("=" * 50)

        # Display players' starting decks
        print(f"{self.game.player1.name} has received cards: "
              f"{[str(card) for card in self.game.player1.deck_of_cards]}")
        print(f"{self.game.player2.name} has received cards: "
              f"{[str(card) for card in self.game.player2.deck_of_cards]}\n")

    def play_turn(self):
        """Play a single turn of the game using the first game's logic."""
        self.turn_count += 1
        print(f"[Round {self.turn_count}]")

        card1 = self.game.player1.get_card()
        card2 = self.game.player2.get_card()

        print(f"{self.game.player1.name} drew {card1}")
        print(f"{self.game.player2.name} drew {card2}")

        # Compare cards and determine the round winner
        if card1 > card2:
            winner = self.game.player1
        else:
            winner = self.game.player2

        winner.add_card(card1)
        winner.add_card(card2)
        print(f"🏆 Round winner: {winner.name}\n")

        self.print_game_state()

    def print_game_state(self):
        """Display the current state of the game."""
        print("-" * 50)
        print(f"📜 {self.game.player1.name}: {len(self.game.player1.deck_of_cards)} cards")
        print(f"📜 {self.game.player2.name}: {len(self.game.player2.deck_of_cards)} cards")
        print("-" * 50)

    def play_game(self):
        """Control the overall game flow."""
        print("🎮 Starting The Game... 🎮")
        self.turn_count = 0

        for _ in range(GAME_ROUNDS):
            if not self.game.player1.deck_of_cards or not self.game.player2.deck_of_cards:
                print("🔥 Game Over - One player has no cards left 🔥")
                break
            self.play_turn()

        # Determine the overall winner
        print("\n🔥 Game Over! 🔥")
        self.declare_winner()

    def declare_winner(self):
        """Declare the game winner based on the number of cards."""
        player1_cards = len(self.game.player1.deck_of_cards)
        player2_cards = len(self.game.player2.deck_of_cards)

        print(f"{self.game.player1.name} has {player1_cards} cards.")
        print(f"{self.game.player2.name} has {player2_cards} cards.")

        if player1_cards > player2_cards:
            print(f"🎉 The winner is {self.game.player1.name}! 🎉")
        elif player1_cards < player2_cards:
            print(f"🎉 The winner is {self.game.player2.name}! 🎉")
        else:
            print("🤝 It's a tie!")

# Run the game
if __name__ == "__main__":
    main_game = CardGameMain()
    main_game.start_game()
    main_game.play_game()
