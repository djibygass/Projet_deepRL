
import time
from game import CantStopGame
from players import RandomPlayer

def simulate_game():
    game = CantStopGame()
    player = RandomPlayer()
    while not game.is_over():
        game.roll_dice()  # Roll the dice
        possible_choices = game.possible_choices  # Get possible choices based on dice roll
        idx = player.choose_columns(possible_choices)  # Choose an index from possible choices
        game.select_choice(idx)  # Update the game based on chosen index
        if player.decide_continue() == False:
            break
    return game.get_winner()

def main():
    num_games = 1000
    start_time = time.time()
    for _ in range(num_games):
        simulate_game()
    end_time = time.time()
    duration = end_time - start_time
    games_per_second = num_games / duration
    print(f"Simulation played {num_games} games in {duration:.2f} seconds ({games_per_second:.2f} games/second)")

if __name__ == "__main__":
    main()
