import tkinter as tk
import random
from game import CantStopGame



class CantStopGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Can't Stop Game")
        self.game = CantStopGame()
        self.current_player = '1'

        # Display whose turn it is
        self.turn_label = tk.Label(self.root, text="Player 1's Turn", font=('Arial', 16))
        self.turn_label.pack(pady=20)

        # Create board
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        self.columns = []
        for i, col in enumerate(self.game.board.columns):
            column_frame = tk.Frame(self.board_frame)
            column_frame.grid(row=0, column=i)
            col_buttons = []
            for j in range(col.length):
                b = tk.Button(column_frame, text="", width=5, height=2, bg="white", fg="black")
                b.grid(row=j, column=0)
                col_buttons.append(b)
            self.columns.append(col_buttons)

            # Add column number below the column
            label = tk.Label(self.board_frame, text=str(col.number))
            label.grid(row=1, column=i)

        # Create dice and action buttons
        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack(pady=20)

        self.roll_button = tk.Button(self.control_frame, text="Roll Dice", command=self.roll_dice)
        self.roll_button.grid(row=0, column=0, padx=20)

        self.dice_label = tk.Label(self.control_frame, text="Dice: ")
        self.dice_label.grid(row=0, column=1, padx=20)

        self.choices_frame = tk.Frame(self.control_frame)
        self.choices_frame.grid(row=1, column=0, columnspan=2)

        self.update_board_display()

        self.decision_frame = tk.Frame(self.control_frame)
        self.decision_frame.grid(row=2, column=0, columnspan=2)

        self.continue_button = tk.Button(self.decision_frame, text="Continue", command=self.roll_dice,
                                         state=tk.DISABLED)
        self.continue_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(self.decision_frame, text="Stop", command=self.stop_turn, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT)

    def roll_dice(self):
        self.game.roll_dice()
        self.update_dice_display()

        # Disable the "Continue" and "Stop" buttons when rolling dice
        self.continue_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.DISABLED)

    def random_move(self):
        # Simulez le lancer de dés pour le joueur aléatoire
        self.roll_dice()

        # Obtenez les choix possibles
        choices = self.game.get_possible_choices()

        # Si le joueur aléatoire a des choix possibles, sélectionnez-en un au hasard
        if choices:
            random_choice = random.choice(choices)
            idx = choices.index(random_choice)
            self.select_choice(idx)

    def stop_turn(self):
        if self.turn_label.cget("text") == "Player 1's Turn":
            self.turn_label.config(text="Random's Turn")

            # Simulez le mouvement du joueur aléatoire
            self.random_move()

            # Après un délai (par exemple 2000 ms = 2 secondes), revenez au tour du joueur 1
            self.root.after(2000, lambda: self.turn_label.config(text="Player 1's Turn"))
        else:
            self.turn_label.config(text="Player 1's Turn")

        # Activez le bouton de lancer de dés pour le prochain joueur
        self.roll_button.config(state=tk.NORMAL)
        self.continue_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.DISABLED)

    def update_dice_display(self):
        dice_text = "Dice: " + " ".join(map(str, self.game.current_dice))
        self.dice_label.config(text=dice_text)
        self.display_choices()

    def display_choices(self):
        for widget in self.choices_frame.winfo_children():
            widget.destroy()

        for idx, choice in enumerate(self.game.get_possible_choices()):
            button_text = " {}, {}".format(choice[1][0], choice[1][1])
            b = tk.Button(self.choices_frame, text=button_text, command=lambda i=idx: self.select_choice(i))
            b.pack(pady=5)

        self.roll_button.config(state=tk.DISABLED)

    def switch_player(self):
        if self.current_player == '1':
            self.current_player = 'R'
            self.turn_label.config(text="Random Player's Turn")
        else:
            self.current_player = '1'
            self.turn_label.config(text="Player 1's Turn")

    def select_choice(self, idx):
        choice = self.game.possible_choices[idx]
        print("Choice combinations:", choice[0])
        print("Choice sums:", choice[1])

        # Use the marker of the current player for both columns
        current_marker = '1' if self.current_player == "Player 1" else 'R'

        column_1 = self.game.board.get_column(choice[1][0])
        column_1.place_marker(current_marker)

        column_2 = self.game.board.get_column(choice[1][1])
        column_2.place_marker(current_marker)

        self.update_board_display()

        # After selecting a choice, enable the "Continue" and "Stop" buttons
        self.continue_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.NORMAL)

    def update_board_display(self):
        for i, col in enumerate(self.game.board.columns):
            for j in range(col.length):
                if col.cells[j] == '1':
                    self.columns[i][j].config(bg="red", text='1')
                elif col.cells[j] == 'R':
                    self.columns[i][j].config(bg="green", text='R')
                else:
                    self.columns[i][j].config(bg="white", text='.')

    def display_board(self):
        for idx, column in enumerate(self.game.board.columns):
            for row, cell in enumerate(column.cells):
                button = tk.Button(self.root, text=cell, width=2, height=1, bg='white', fg='black')
                button.grid(row=row, column=idx)
            label = tk.Label(self.root, text=str(column.number))
            label.grid(row=len(column.cells), column=idx)


if __name__ == "__main__":
    root = tk.Tk()
    gui = CantStopGUI(root)
    root.mainloop()
