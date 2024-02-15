import itertools

from dice import Dice
from scoresheet import Scoresheet
import random


class Player:
    def __init__(self, name):
        self.name = name
        self.scoresheet = Scoresheet()
        self.dice = [Dice() for _ in range(3)]  # Dice objects for rolling
        self.dice_results = []  # To store results of dice rolls
        self.rerolls_remaining = 2  # Players are allowed up to two rerolls

    def roll_dice(self):
        # Roll all dice and store the results
        self.dice_results = [dice.roll() for dice in self.dice]
        return self.dice_results

    def choose_dice_to_keep(self, rolled_dice):
        # This method should be overridden in subclasses for human and AI players
        # For a human player, you would prompt for input
        # For an AI player, you would implement some strategy for choosing dice
        raise NotImplementedError("This method should be overridden in a subclass")

    def take_turn(self, game_logic):
        # Roll initial set of dice
        roll_results = self.roll_dice()
        print(f"{self.name} rolled: {roll_results}")

        # Player decides which dice to keep
        dice_to_keep_indices = self.choose_dice_to_keep(roll_results)
        print(f"{self.name} kept: {dice_to_keep_indices}")

        # Handle rerolls if necessary
        if dice_to_keep_indices != list(range(len(self.dice))):
            self.reroll(dice_to_keep_indices)

        # Record roll results in the scoresheet
        self.scoresheet.record_roll(roll_results)

    def reroll(self, kept_dice_indices, is_final_reroll=False):
        # Keep the results of the dice that were chosen to be retained
        kept_dice_results = [self.dice_results[i] for i in kept_dice_indices if i != -1]

        # Determine the number of new dice to roll
        num_new_dice = (len(self.dice) - len(kept_dice_results)) + 1

        # For the final reroll, if any, ensure total dice count is five
        if is_final_reroll:
            num_new_dice = 5 - len(kept_dice_results)

        # Roll the new dice
        new_dice_results = [self.roll_single_dice() for _ in range(num_new_dice)]

        # Combine kept and new dice results
        self.dice_results = kept_dice_results + new_dice_results
        self.rerolls_remaining -= 1

        return self.dice_results

    def roll_single_dice(self):
        # Randomly choose a new side
        return random.choice(Dice.die_faces)


class HumanPlayer(Player):

    def choose_dice_to_keep(self, rolled_dice):
        print("Choose which dice to keep (enter indices separated by a space), or type 'all' to keep all:")
        input_str = input().strip().lower()
        if input_str == 'all':
            return list(range(len(rolled_dice)))
        else:
            return list(map(int, input_str.split()))


class RandomAIPlayer(Player):
    def choose_dice_to_keep(self, rolled_dice):
        # Generate all possible combinations of dice indices
        num_dice = len(rolled_dice)
        possible_choices = []
        for i in range(num_dice):  # Generate combinations for keeping none to keeping all but one
            possible_choices.extend(itertools.combinations(range(num_dice), i))

        # Add the option to keep all dice
        possible_choices.append(tuple(range(num_dice)))  # This represents keeping all dice

        # Randomly select one of the possible choices
        chosen_combination = random.choice(possible_choices)
        dice_to_keep_indices = list(chosen_combination)

        print(f"{self.name} chooses to keep dice at indices: {dice_to_keep_indices}")
        return dice_to_keep_indices
