from src.environments.bandido_v2.settings import setup_loader
from src.environments.bandido_v2 import table, deck, hand


class BandidoGame:
    def __init__(self):
        self.loader = setup_loader()
        self.game_table = table()
        self.game_deck = deck()
        self.player_hand = hand()
        # Initialize other necessary attributes

    def reset(self):
        """Reset the game to its initial state."""
        # Reset table, deck, and other attributes

    def take_turn(self, player):
        """Execute a single turn for a player."""
        # Let the player select an action (or compute action for AI)
        # Update game state based on selected action

    def is_game_over(self):
        """Check if the game has ended."""
        # Implement the game-ending conditions
        return False

    def play(self):
        """Main game loop."""
        while not self.is_game_over():
            # For now, let's assume there are two players: 'human' and 'computer'
            for player in ['human', 'computer']:
                self.take_turn(player)


if __name__ == "__main__":
    game = BandidoGame()
    game.play()
