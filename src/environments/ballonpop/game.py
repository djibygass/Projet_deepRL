import random
from player import HumanPlayer, RandomAIPlayer
from game_logic import GameLogic
from game_interface import GameInterface
from typing import List


class Game:
    def __init__(self):
        self.game_logic = None
        self.game_interface = None

    def setup_game(self, player_names: List[str]):

        # Create players and initialize game_logic with them
        players = [HumanPlayer(name) if name == "Human" else RandomAIPlayer(name) for name in player_names]
        self.game_logic = GameLogic(players)

        # Initialize GameInterface with the game logic instance
        self.game_interface = GameInterface(self.game_logic)

    # def start_game(self):
    #     while not self.game_logic.is_game_over():
    #         self.game_interface.display_board()
    #
    #         current_player = self.game_logic.next_player()
    #         print(f"\n{current_player.name}'s turn:")
    #
    #         # Roll dice and display results
    #         roll_results = current_player.roll_dice()
    #         print(f"{current_player.name} rolled: {roll_results}")
    #
    #         # Handle dice keeping and rerolling
    #         dice_to_keep = current_player.choose_dice_to_keep(roll_results)
    #         if len(dice_to_keep) < len(current_player.dice):
    #             roll_results = current_player.reroll(dice_to_keep)
    #             print(f"{current_player.name} rerolled and got: {roll_results}")
    #
    #         # Record the roll results in the scoresheet
    #         current_player.scoresheet.record_roll(roll_results)
    #
    #         # Check for the game end condition and display board after turn
    #         if self.game_logic.is_game_over():
    #             self.game_interface.show_end_game_results(
    #                 {p.name: p.scoresheet.get_current_score() for p in self.game_logic.players})
    #             break
    #
    #         # Print a separator line after each turn
    #         print("\n" + "-" * 70)

    def start_game(self):
        while not self.game_logic.is_game_over():
            self.game_interface.display_board()

            current_player = self.game_logic.next_player()
            print(f"\n{current_player.name}'s turn:")

            # Delegate the turn logic to the GameLogic class
            self.game_logic.play_turn(current_player)

            # Check for the game end condition and display board after turn
            if self.game_logic.is_game_over():
                self.game_interface.show_end_game_results(
                    {p.name: p.scoresheet.get_current_score() for p in self.game_logic.players})
                break

            # Print a separator line after each turn
            print("\n" + "-" * 70)


if __name__ == "__main__":
    game = Game()
    #game.setup_game(["Human"])
    #game.setup_game(["Human", "RandomAI"])
    game.setup_game(["RandomAI"])
    game.start_game()


import time

# if __name__ == "__main__":
#     start_time = time.time()  # Get the current time
#     games_played = 0  # Initialize a counter for the number of games
#
#     while time.time() - start_time < 1:  # Loop for one second
#         game = Game()
#         game.setup_game(["RandomAI"])
#         game.start_game()
#         games_played += 1  # Increment the counter after each game
#
#     print(f"Number of games played in one second: {games_played}")


# import time
#
# if __name__ == "__main__":
#     total_games = 5  # Number of games to play for the test
#     total_time_taken = 0
#
#     for _ in range(total_games):
#         start_time = time.time()
#
#         game = Game()
#         game.setup_game(["RandomAI"])
#         game.start_game()
#
#         end_time = time.time()
#         total_time_taken += (end_time - start_time)
#
#     avg_time_per_game = total_time_taken / total_games
#     games_per_second = 1 / avg_time_per_game if avg_time_per_game > 0 else float('inf')
#
#     print(f"Average time per game: {avg_time_per_game:.4f} seconds")
#     print(f"Estimated number of games per second: {games_per_second:.2f}")
