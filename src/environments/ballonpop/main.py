# main.py
from game_logic import Game

if __name__ == "__main__":
    # Initialize the game with the required number of players
    game = Game(number_of_players=1)  # If it's a solo game
    game.play_game()
