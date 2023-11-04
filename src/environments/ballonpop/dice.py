# dice.py
import random


class Dice:
    # A die has six sides, with each side showing a color and a shape
    die_faces = [
        ("Red", "Star"),
        ("Red", "Moon"),
        ("Red", "Diamond"),
        ("Blue", "Star"),
        ("Blue", "Moon"),
        ("Yellow", "Star")
    ]

    @staticmethod
    def roll(number_of_dice=1):
        # Roll the specified number of dice and return the results
        return [random.choice(Dice.die_faces) for _ in range(number_of_dice)]


# Example usage in the main game loop or testing
if __name__ == "__main__":
    # Simulate rolling the dice three times
    for _ in range(1):
        results = Dice.roll(3)
        for color, shape in results:
            print(f"Rolled a {color} balloon with a {shape}.")
