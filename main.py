from CardGame import CardGame

class CardGameMain:
    def __init__(self):
        self.game = None
        self.turn_count = 0  # Initialize turn counter

    def start_game(self, player1_name, player2_name):
        self.game = CardGame(player1_name, player2_name)
        print("=" * 50)
        print(f"🎴 The Game has Started! 🎴")
        print(f"Players: {player1_name} vs {player2_name}")
        print("=" * 50)
        self.print_game_state()

    def play_turn(self):
        if not self.game.player1.hand or not self.game.player2.hand:
            print("🔥 Game Over 🔥")
            return

        self.turn_count += 1  # Increment turn counter
        print(f"\n[Turn {self.turn_count}]")  # Display turn number

        card1 = self.game.player1.get_card(0)
        card2 = self.game.player2.get_card(0)
        result = f"{self.game.player1.name} played {card1}, {self.game.player2.name} played {card2}.\n"

        if card1.value > card2.value:
            self.game.player1.add_card(card1)
            self.game.player1.add_card(card2)
            result += f"🏆 {self.game.player1.name} wins this turn!"
        elif card1.value < card2.value:
            self.game.player2.add_card(card1)
            self.game.player2.add_card(card2)
            result += f"🏆 {self.game.player2.name} wins this turn!"
        else:
            self.game.player1.add_card(card1)
            self.game.player2.add_card(card2)
            result += "🤝 It's a tie! Both cards are returned to the players."

        print(result)
        self.print_game_state()

    def print_game_state(self):
        print("-" * 50)
        print(f"📜 {self.game.player1.name}: {len(self.game.player1.hand)} cards")
        print(f"📜 {self.game.player2.name}: {len(self.game.player2.hand)} cards")
        total_cards = len(self.game.player1.hand) + len(self.game.player2.hand)
        print(f"🔢 Total cards in play: {total_cards}")
        print("-" * 50)

    def play_game(self):
        print("🎮 Starting The Game... 🎮")
        max_turns = 20
        self.turn_count = 0  # Reset turn counter

        while self.game.player1.hand and self.game.player2.hand:
            self.play_turn()
            if self.turn_count >= max_turns:
                print("⏳ Game stopped due to too many turns.")
                break

        print("\n🔥 Game Over! 🔥")
        print(f"{self.game.player1.name} has {len(self.game.player1.hand)} cards.")
        print(f"{self.game.player2.name} has {len(self.game.player2.hand)} cards.")

        if len(self.game.player1.hand) > len(self.game.player2.hand):
            print(f"🎉 The winner is {self.game.player1.name}! 🎉")
        elif len(self.game.player1.hand) < len(self.game.player2.hand):
            print(f"🎉 The winner is {self.game.player2.name}! 🎉")
        else:
            print("🤝 It's a tie!")

# Start the game
main_game = CardGameMain()
main_game.start_game("Alice", "Bob")
main_game.play_game()
