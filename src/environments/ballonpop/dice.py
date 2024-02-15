import random


class Dice:
    die_faces = [
        ("Red", "Star"),
        ("Red", "Moon"),
        ("Red", "Diamond"),
        ("Blue", "Star"),
        ("Blue", "Moon"),
        ("Yellow", "Star")
    ]

    def __init__(self):
        self.current_side = None

    def roll(self):
        self.current_side = random.choice(Dice.die_faces)
        return self.current_side


# Main game loop or testing
if __name__ == "__main__":
    dice_objects = [Dice() for _ in range(3)]  # Create a list of three Dice objects
    for _ in range(1):  # Suppose we roll the dice once per round
        roll_results = [dice.roll() for dice in dice_objects]
        for result in roll_results:
            print(f"Rolled a {result[0]} balloon with a {result[1]}.")

