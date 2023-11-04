class Player:
    def __init__(self, name):
        self.name = name
        self.scoresheet = Scoresheet()
        self.dice_rolled = []  # Store the dice results
        self.re_rolls = 0  # Track the number of re-rolls

    def take_turn(self):
        # Roll three dice initially
        self.dice_rolled = Dice.roll(3)
        self.evaluate_roll()

        # Offer the chance to re-roll
        while self.re_rolls < 2:  # Allow up to two re-rolls
            if self.want_to_reroll():
                self.re_rolls += 1
                additional_dice = 1  # Must roll an additional die on a re-roll
                self.dice_rolled.extend(Dice.roll(additional_dice))
                self.evaluate_roll()
            else:
                break

        # Once done, record the roll to the scoresheet
        self.scoresheet.record_roll(self.dice_rolled)

    def evaluate_roll(self):
        # Evaluate the dice roll here and decide whether to re-roll or not
        # This method would likely interact with the game interface to inform the player
        # of their roll and ask if they want to re-roll.
        pass

    def want_to_reroll(self):
        # Method to ask the player (or determine, if AI) if they want to re-roll
        # This would return True if the player wants to re-roll, False otherwise
        # For now, we can simulate this with user input or a simple AI decision logic
        # Example user input version:
        response = input("Do you want to re-roll? (y/n): ")
        return response.lower().startswith('y')

    # Additional methods as necessary...
