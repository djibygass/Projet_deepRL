import random
from itertools import permutations
import copy

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
        possible_combinations = set([
            (dice[0] + dice[1], dice[2] + dice[3]),
            (dice[0] + dice[2], dice[1] + dice[3]),
            (dice[0] + dice[3], dice[1] + dice[2])
        ])
        self.possible_choices = [(combination, sums) for combination, sums in
                                 zip([(dice[0], dice[1]), (dice[0], dice[2]), (dice[0], dice[3])],
                                     possible_combinations)]

        # Filtrer les doublons
        self.possible_choices = list(dict.fromkeys(self.possible_choices))

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
        # Compter combien de colonnes un joueur a atteint le sommet
        player_columns_reached = 0
        for column in self.board.columns:
            if column.cells[-1] == self.current_player:  # Vérifier le sommet de la colonne
                player_columns_reached += 1
        return player_columns_reached >= 3

    def get_winner(self):
        if self.is_over():
            return self.current_player
        return None

    def encode_game_state(self):
        """
        Encode the state of the CantStopGame into a vector representation.
        """
        encoding = []

        # Parcourir chaque colonne et ajouter l'état de chaque cellule
        for column in self.board.columns:
            for cell in column.cells:
                if cell == self.current_player:
                    encoding.append(1)  # Marqueur du joueur actuel
                elif cell == '.':
                    encoding.append(0)  # Cellule vide
                else:
                    encoding.append(-1)  # Marqueur de l'autre joueur

        # Ajouter les valeurs des dés
        encoding.extend(self.current_dice)

        # Ajouter l'information du joueur actuel
        encoding.append(1 if self.current_player == "1" else -1)

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
        all_actions = dice_values.generate_all_possible_actions(dice_values)
        encoding = [0] * len(all_actions)
        action_index = all_actions.index(selected_action)
        encoding[action_index] = 1
        return encoding

    def clone(self):
        # Crée une nouvelle instance de CantStopGame
        cloned_game = CantStopGame()

        # Copie profonde du plateau de jeu
        cloned_game.board = copy.deepcopy(self.board)

        # Copie des dés actuels et des choix possibles
        cloned_game.current_dice = self.current_dice[:]
        cloned_game.possible_choices = self.possible_choices[:]

        # Copie du joueur actuel
        cloned_game.current_player = self.current_player

        return cloned_game

