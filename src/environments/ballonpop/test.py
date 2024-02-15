class Scoresheet:
    # ...

    def calculate_total_score(self):
        # Sum up the scores from all breaks
        self.total_score = sum(self.breaks)

    # ... (rest of the Scoresheet methods)




# In your game loop (in Game class or main game logic)
while not self.game_logic.all_breaks_triggered():
    # Existing game logic here
    # ...

# In GameLogic class
def all_breaks_triggered(self):
    return all(player.scoresheet.num_breaks_triggered >= 3 for player in self.players)




# In your game loop, after the game ends
for player in self.game_logic.players:
    self.game_interface.display_board_for_player(player.scoresheet)
    print("--------------------")

# Determine and announce the winner
# ...

# In GameInterface class
def display_board_for_player(self, scoresheet):
    # Display the scoresheet for a single player
    # ...

    # In your game loop, after the game ends
    for player in self.game_logic.players:
        self.game_interface.display_board_for_player(player.scoresheet)
        print("--------------------")

    # Determine and announce the winner
    # ...

    # In GameInterface class
    def display_board_for_player(self, scoresheet):
# Display the scoresheet for a single player
# ...
