import time
from game import CantStopGame
from players import MCTSPlayer
from players import RandomPlayer


def simulate_game():
    game = CantStopGame()
    player = MCTSPlayer()
    while not game.is_over():
        game.roll_dice()
        possible_choices = game.get_possible_choices()
        idx = player.choose_columns(game)
        game.select_choice(idx)

        if not player.decide_continue(game):
            break

    return game.get_winner()
def count_mcts_victories(num_games):
    mcts_victories = 0
    for _ in range(num_games):
        winner = simulate_game()
        if winner == '1':  # Supposons que '1' représente le MCTSPlayer
            mcts_victories += 1

    print(f"MCTSPlayer a gagné {mcts_victories} fois sur {num_games} parties.")
    return mcts_victories
def main():
    num_games = 100
    start_time = time.time()
    for _ in range(num_games):
        simulate_game()
    end_time = time.time()
    duration = end_time - start_time
    games_per_second = num_games / duration
    count_mcts_victories(num_games)
    print(f"Simulation played {num_games} games in {duration:.2f} seconds ({games_per_second:.2f} games/second)")

if __name__ == "__main__":
    main()
