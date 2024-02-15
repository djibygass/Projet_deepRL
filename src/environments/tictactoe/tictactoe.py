import random

# Initialize the Tic-Tac-Toe board
board = [" " for _ in range(9)]

# Function to display the Tic-Tac-Toe board
def display_board():
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

# Function to check if the board is full
def is_board_full():
    return " " not in board

# Function to check if a player has won
def check_winner(player):
    win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6)]

    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False

# Function for the computer's move (random)
def computer_move():
    empty_cells = [i for i, cell in enumerate(board) if cell == " "]
    return random.choice(empty_cells)

# Main game loop
def play_game():
    player = "X"
    computer = "O"
    current_player = player

    while True:
        display_board()

        if current_player == player:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move >= 9 or board[move] != " ":
                print("Invalid move. Try again.")
                continue
        else:
            print("Computer's turn:")
            move = computer_move()

        board[move] = current_player

        if check_winner(current_player):
            display_board()
            print(f"{current_player} wins!")
            break
        elif is_board_full():
            display_board()
            print("It's a tie!")
            break

        current_player = player if current_player == computer else computer

if __name__ == "__main__":
    play_game()
