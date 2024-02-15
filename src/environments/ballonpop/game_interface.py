from game_logic import GameLogic


class GameInterface:
    def __init__(self, game):
        self.game_logic = game

    def display_board(self):
        for player in self.game_logic.players:
            print(f"\n{player.name}'s Scoresheet:")
            for color, scores in player.scoresheet.scoresheet.items():
                position = player.scoresheet.current_positions[color]
                score_string = " ".join(
                    [f"[{score}]" if idx == position else str(score) for idx, score in enumerate(scores)])
                print(f"{color}: {score_string}")

            print("-" * 20)  # Separator line
            breaks_string = " | ".join(f"Break {i + 1}: {score}" for i, score in enumerate(player.scoresheet.breaks))
            print(f"Breaks: {breaks_string}")
            print(f"Total Score: {player.scoresheet.total_score}")
            print("-" * 20)  # Separator line

    def get_player_input(self, prompt):
        # Get input from the player; this can be more complex in a GUI
        return input(prompt)

    def show_end_game_results(self, final_scores):
        # Display the final scores and the winner
        print("Game Over! Final scores:")
        for player, score in final_scores.items():
            print(f"{player}: {score}")
        winner = max(final_scores, key=final_scores.get)
        print(f"The winner is {winner}!")


    #def display_board_for_player
