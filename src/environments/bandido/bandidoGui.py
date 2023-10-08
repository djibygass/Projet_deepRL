import numpy as np
import matplotlib.pyplot as plt

# Define the board size
board_width = 22
board_height = 11

# Initialize the board with all zeros
board = np.zeros((board_height, board_width))

# Define the supercard with 5 exits
supercard_5 = [
    [0, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 1],
    [0, 1, 0, 0, 1, 0]
]

# Define the supercard with 6 exits (just for reference, we'll use the 5 exit one for now)
supercard_6 = [
    [0, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 1],
    [0, 1, 0, 0, 1, 0]
]

# Place the supercard in the center of the board
center_row = (board_height - 3) // 2
center_col = (board_width - 6) // 2

board[center_row:center_row+3, center_col:center_col+6] = supercard_5

# Plotting the board
fig, ax = plt.subplots(figsize=(10,5))
cax = ax.matshow(board, cmap='gray_r')
plt.xticks(np.arange(0, board_width, 1))
plt.yticks(np.arange(0, board_height, 1))
ax.set_xticks(np.arange(-.5, board_width, 1), minor=True)
ax.set_yticks(np.arange(-.5, board_height, 1), minor=True)
ax.grid(which='minor', color='black', linestyle='-', linewidth=2)
plt.show()
