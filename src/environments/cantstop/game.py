import random
from itertools import permutations


class Column:
    def __init__(self, number, length):
        self.number = number
        self.length = length
        self.cells = ['.' for _ in range(length)]

    def place_marker(self, player):
        for idx, cell in enumerate(self.cells):
            if cell == '.':
                self.cells[idx] = player
                return


class CantStopBoard:
    def __init__(self):
        self.columns = [Column(i, l) for i, l in zip(range(2, 13), [3, 5, 7, 9, 11, 13, 11, 9, 7, 5, 3])]

    def get_column(self, number):
        for col in self.columns:
            if col.number == number:
                return col


class CantStopGame:
    def __init__(self):
        self.board = CantStopBoard()
        self.current_dice = [1, 1, 1, 1]
        self.possible_choices = []
        self.current_player = '1'  # Start with player '1'

    def roll_dice(self):
        self.current_dice = [random.randint(1, 6) for _ in range(4)]
        self.possible_choices = []  # Reset possible choices
        self.get_possible_choices()  # Generate new choices based on the new dice roll

    def get_possible_choices(self):
        if self.possible_choices:
            return self.possible_choices

        dice = self.current_dice
        possible_combinations = [
            (dice[0] + dice[1], dice[2] + dice[3]),
            (dice[0] + dice[2], dice[1] + dice[3]),
            (dice[0] + dice[3], dice[1] + dice[2])
        ]
        self.possible_choices = [(combination, sums) for combination, sums in
                                 zip([(dice[0], dice[1]), (dice[0], dice[2]), (dice[0], dice[3])],
                                     possible_combinations)]

        return self.possible_choices

    def select_choice(self, idx):
        choice = self.possible_choices[idx]
        column_1 = self.board.get_column(choice[1][0])
        column_1.place_marker(self.current_player)
        column_2 = self.board.get_column(choice[1][1])
        column_2.place_marker(self.current_player)

        # Switch the current player for the next turn
        self.current_player = 'R' if self.current_player == '1' else '1'

    def is_over(self):
        # Count how many columns a player has reached the top
        player_columns_reached = 0
        for column in self.board.columns:
            if column.cells[0] == self.current_player:
                player_columns_reached += 1
        return player_columns_reached >= 3

    def get_winner(self):
        if self.is_over():
            return self.current_player
        return None

    def encode_game_state(game):
        """
        Encode the state of the CantStopGame into a vector representation.

        :param game: An instance of the CantStopGame.
        :return: A list representing the encoded state.
        """

        # Initialize the encoding list
        encoding = []

        # 1. Add the position of the pions for each column
        for col in range(2, 13):
            # Assuming the game board is a dictionary with keys being column numbers
            # and values being a tuple (player1_position, player2_position)
            encoding.append(game.board.get(col, (0, 0))[0])  # Player 1
            encoding.append(game.board.get(col, (0, 0))[1])  # Player 2

        # 2. Add the position of the temporary pions for each column
        # Assuming the temporary pions are stored similarly to the main board
        for col in range(2, 13):
            encoding.append(game.temp_pions.get(col, (0, 0))[0])  # Player 1
            encoding.append(game.temp_pions.get(col, (0, 0))[1])  # Player 2

        # 3. Add dice values
        encoding.extend(game.dice_values)

        # 4. Add the current player information
        encoding.append(1 if game.current_player == "Player 1" else -1)

        return encoding

    def generate_all_possible_actions(dice_values):
        """
        Generate all possible actions based on the dice values.

        :param dice_values: A list containing four dice values.
        :return: A list of tuples representing all possible actions.
        """
        all_actions = set()
        for perm in permutations(dice_values, 4):
            action_1 = perm[0] + perm[1]
            action_2 = perm[2] + perm[3]
            all_actions.add((action_1, action_2))
        return sorted(list(all_actions))

    def one_hot_encode_action(dice_values, selected_action):
        """
        One-hot encode a specific action based on the dice values.

        :param dice_values: A list containing four dice values.
        :param selected_action: A tuple representing the selected action.
        :return: A list representing the one-hot encoded action.
        """
        all_actions = generate_all_possible_actions(dice_values)
        encoding = [0] * len(all_actions)
        action_index = all_actions.index(selected_action)
        encoding[action_index] = 1
        return encoding
