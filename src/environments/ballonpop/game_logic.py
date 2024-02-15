from typing import Optional, List, Tuple, Dict
from player import Player, RandomAIPlayer


class GameLogic:
    def __init__(self, players: List[Player], max_dice: int = 5):
        self.players = players
        self.current_player_index = 0
        self.max_dice = max_dice

    def next_player(self):
        player = self.players[self.current_player_index]
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        return player

    def initial_roll(self) -> List[Tuple[str, str]]:
        # The current player rolls their initial set of dice
        player = self.players[self.current_player_index]
        return player.roll_dice()

    def handle_rerolls(self, dice_to_keep: List[int], rolled_dice: List[Tuple[str, str]]) -> None:
        # The current player handles rerolls based on their decision
        player = self.players[self.current_player_index]
        if dice_to_keep:
            rerolled_dice = player.reroll(dice_to_keep)
            # Combine the kept dice and the rerolled dice
            player.scoresheet.record_roll(rolled_dice[:len(dice_to_keep)] + rerolled_dice)

    def record_and_score(self, roll_results: List[Tuple[str, str]]) -> int:
        # Record the roll results and calculate the score
        player = self.players[self.current_player_index]
        player.scoresheet.record_roll(roll_results)
        return player.scoresheet.get_current_score()

    def check_for_end_of_game(self) -> Optional[Dict[str, int]]:
        # Check if the game has reached its end condition
        if any(player.scoresheet.breaks >= 3 for player in self.players):
            return {player.name: player.scoresheet.get_current_score() for player in self.players}
        return None

    @staticmethod
    def get_valid_indices(prompt, valid_indices):
        while True:
            input_str = input(prompt).strip().lower()
            if input_str == 'all':
                return valid_indices
            else:
                try:
                    indices = [int(idx) for idx in input_str.split()]
                    if all(idx in valid_indices for idx in indices):
                        return indices
                    else:
                        print("Invalid indices, please try again.")
                except ValueError:
                    print("Invalid input, please try again.")

    def play_turn(self, player):
        player.rerolls_remaining = 2

        # Initial roll
        initial_roll = player.roll_dice()
        print(f"{player.name} rolled: {initial_roll}")

        # First decision on which dice to keep
        dice_to_keep = player.choose_dice_to_keep(initial_roll)
        print(f"{player.name} decided to keep: {[initial_roll[i] for i in dice_to_keep]}")

        if len(dice_to_keep) < len(player.dice):
            # Perform the first reroll
            reroll_results = player.reroll(dice_to_keep)
            print(f"{player.name} rerolled and got: {reroll_results}")

            if player.rerolls_remaining > 0:
                new_dice_indices = list(range(len(dice_to_keep), len(reroll_results)))

                if isinstance(player, RandomAIPlayer):
                    # Extract the new rerolled dice based on new_dice_indices
                    new_rerolled_dice = [reroll_results[i] for i in new_dice_indices]
                    second_decision_indices = player.choose_dice_to_keep(new_rerolled_dice)
                    second_decision_indices = [i + len(dice_to_keep) for i in second_decision_indices]
                    print(f"{player.name} chooses to keep new dice at indices: {second_decision_indices}")
                else:
                    # Human player makes decision
                    second_decision_indices = self.get_valid_indices(
                        f"{player.name}, choose which of the new rerolled dice to keep (indices {new_dice_indices}), or type 'all' to keep all:",
                        new_dice_indices
                    )

                if set(second_decision_indices) == set(new_dice_indices):
                    # If 'all' new dice are kept, skip the final reroll
                    print(f"{player.name} decides to keep all rerolled dice and not reroll again.")
                else:
                    # Combine kept dice from both rolls for the final reroll
                    final_kept_dice_indices = dice_to_keep + second_decision_indices

                    # Ensure total dice count is five for the final reroll
                    additional_dice_needed = 5 - len(final_kept_dice_indices)
                    final_kept_dice_indices += [-1] * additional_dice_needed

                    final_reroll_results = player.reroll(final_kept_dice_indices, is_final_reroll=True)
                    print(f"{player.name} made a final reroll and got: {final_reroll_results}")
            else:
                print(f"{player.name} has no rerolls remaining.")
        else:
            print(f"{player.name} decides not to reroll.")

        # Record the final roll in the scoresheet
        player.scoresheet.record_roll(player.dice_results)

    def is_game_over(self):
        # Check if any player has triggered 3 breaks
        return any(player.scoresheet.num_breaks_triggered >= 3 for player in self.players)

    # def all_breaks_triggered(self):
    #     return all(player.scoresheet.num_breaks_triggered >= 3 for player in self.players)
