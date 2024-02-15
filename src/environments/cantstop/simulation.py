import time
from game import CantStopGame
from players import MCTSPlayer
from players import DQNAgent


def simulate_game(player):
    game = CantStopGame()
    while not game.is_over():
        game.roll_dice()
        possible_choices = game.get_possible_choices()
        idx = player.choose_columns(game)
        game.select_choice(idx)

        if not player.decide_continue(game):
            break

    return game.get_winner()


def count_dqn_victories(player, num_games):
    dqn_victories = 0
    for _ in range(num_games):
        winner = simulate_game(player)
        if winner == '1':  # Update this condition based on how DQN agent's victory is represented
            dqn_victories += 1

    print(f"DQNAgent a gagné {dqn_victories} fois sur {num_games} parties.")
    return dqn_victories


def main():
    num_games = 100
    dqn_agent = DQNAgent(88, 2)  # Define state_size and action_size

    # Simulate games for DQNAgent
    start_time = time.time()
    count_dqn_victories(dqn_agent, num_games)  # Count victories for DQN agent
    end_time = time.time()
    duration = end_time - start_time
    games_per_second = num_games / duration
    print(f"DQNAgent played {num_games} games in {duration:.2f} seconds ({games_per_second:.2f} games/second)")


if __name__ == "__main__":
    main()
