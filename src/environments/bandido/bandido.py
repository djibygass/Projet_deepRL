from src.environments.bandido_cards import cards
import random

class BandidoGame:
    def __init__(self, board_size=20):
        self.board_size = board_size
        self.board = [['.'] * board_size for _ in range(board_size)]
        self.starting_tile_position = (board_size // 2 - 1, board_size // 2 - 3)  # Position adjusted for the 3x6 tile

        self.deck = self.initialize_deck()
        self.hand = [self.draw_card() for _ in range(5)]

    def initialize_deck(self):
        deck = []
        for card_name, card_matrix in cards.items():
            count = 2 if 'x2' in card_name else 1
            deck.extend([card_name] * count)
        random.shuffle(deck)
        return deck

    def draw_card(self):
        if self.deck:
            return self.deck.pop()
        return None

    def place_tile_on_board(self, tile, row, col):
        tile_rows, tile_cols = len(tile), len(tile[0])
        for i in range(tile_rows):
            for j in range(tile_cols):
                self.board[row + i][col + j] = str(tile[i][j])

    def place_starting_tile(self, level="easy"):
        start_tile = cards["SuperCard1"] if level == "easy" else cards["SuperCard2"]
        row_start, col_start = self.starting_tile_position
        self.place_tile_on_board(start_tile, row_start, col_start)

    def display(self):
        for row in self.board:
            print(" ".join(row))

    def rotate_tile(self, tile):
        return list(zip(*tile[::-1]))

    def is_valid_move(self, tile, row, col):
        for _ in range(4):  # Try all four orientations of the tile
            if self.check_tile_placement(tile, row, col):
                return True
            tile = self.rotate_tile(tile)
        return False

    def check_tile_placement(self, tile, row, col):
        if row + len(tile) > self.board_size or col + len(tile[0]) > self.board_size:
            return False

        for i in range(len(tile)):
            for j in range(len(tile[0])):
                if tile[i][j] == "1":
                    if j > 0 and self.board[row + i][col + j - 1] == ".":
                        return False
                    if j < len(tile[0]) - 1 and self.board[row + i][col + j + 1] == ".":
                        return False
                    if i > 0 and self.board[row + i - 1][col + j] == ".":
                        return False
                    if i < len(tile) - 1 and self.board[row + i + 1][col + j] == ".":
                        return False
        return True

    def game_loop(self):
        while True:
            print("Your hand:", self.hand)
            chosen_card_name = input("Choose a card from your hand or type 'exit' to end: ")

            if chosen_card_name == "exit":
                break

            if chosen_card_name not in self.hand:
                print("Invalid card choice. Try again.")
                continue

            row = int(input(f"Enter the row (0-{self.board_size - 1}) to place the {chosen_card_name}: "))
            col = int(input(f"Enter the column (0-{self.board_size - 1}) to place the {chosen_card_name}: "))

            chosen_tile = cards[chosen_card_name]
            if self.is_valid_move(chosen_tile, row, col):
                self.place_tile_on_board(chosen_tile, row, col)
                self.hand.remove(chosen_card_name)
                self.hand.append(self.draw_card())
            else:
                print("Invalid move. Please try again.")

            self.display()

game = BandidoGame()
game.place_starting_tile(level="easy")
game.display()
game.game_loop()  # Uncomment this line to run the game in an interactive mode.
