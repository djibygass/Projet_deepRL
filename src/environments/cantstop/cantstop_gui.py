import tkinter as tk
from tkinter import ttk


class CantStopGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Can't Stop Game")

        # Game board columns structure
        self.columns = {
            2: 3,
            3: 5,
            4: 7,
            5: 9,
            6: 11,
            7: 13,
            8: 11,
            9: 9,
            10: 7,
            11: 5,
            12: 3
        }

        # Create the board
        self.create_board()

        # Dice roll button
        self.roll_button = ttk.Button(root, text="Roll Dice", command=self.roll_dice)
        self.roll_button.grid(row=15, column=0, columnspan=2, pady=20)

        # Display dice results
        self.dice_label = ttk.Label(root, text="Dice: ")
        self.dice_label.grid(row=16, column=0, pady=5)

        # Dropdown for pair choices
        self.choices = ttk.Combobox(root, state="readonly")
        self.choices.grid(row=17, column=0, pady=5)

        # Confirm button for pair choice
        self.confirm_button = ttk.Button(root, text="Confirm", command=self.confirm_choice)
        self.confirm_button.grid(row=18, column=0, pady=5)

    def create_board(self):
        for col, height in self.columns.items():
            label = ttk.Label(self.root, text=f"Column {col}: {'.' * height}")
            label.grid(row=col - 2, column=0, padx=10, pady=5)

    def roll_dice(self):
        # For now, display a mock dice roll
        self.dice_label['text'] = "Dice: 1, 2, 3, 4"

        # Mock pair choices
        choices = ["1-2 and 3-4", "1-3 and 2-4", "1-4 and 2-3"]
        self.choices['values'] = choices

    def confirm_choice(self):
        # Just print the selected choice for now
        print(self.choices.get())


root = tk.Tk()
app = CantStopGUI(root)
root.mainloop()
