
class Board:

    def __init__(self, board_size):
        self.board_size = board_size
        self.board = {}
        self.init_board()

    def init_board(self):
        for i in range(2, self.board_size + 1):
            self.board[i] = 0

    def get_board_size(self):
        return self.board_size

    def set_board_size(self, board_size):
        self.board_size = board_size

    def get_board(self):
        return self.board

    def set_board(self, board):
        self.board = board

    def get_board_value(self, key):
        return self.board[key]

    def set_board_value(self, key, value):
        self.board[key] = value

    def get_board_keys(self):
        return self.board.keys()

    def get_board_values(self):
        return self.board.values()

    def get_board_items(self):
        return self.board.items()

