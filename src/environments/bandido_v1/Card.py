class Card:
    def __init__(self, matrix, name):
        self.original_matrix = matrix
        self.matrix = matrix
        self.name = name
        self.rotation = 0  # Initial rotation is 0°

    def rotate(self, angle=90):
        """
        Rotate the card by a given angle (only right angles are allowed: 90°, 180°, 270°).
        """
        rotations = {
            90: lambda mat: [list(reversed(col)) for col in zip(*mat)],
            180: lambda mat: [list(reversed(row)) for row in reversed(mat)],
            270: lambda mat: [list(col) for col in reversed(list(zip(*mat)))]
        }
        if angle not in rotations:
            raise ValueError("Only rotations of 90°, 180°, and 270° are allowed.")

        self.rotation = (self.rotation + angle) % 360
        self.matrix = rotations[angle](self.matrix)

    def __str__(self):
        return '\n'.join([''.join([str(cell) for cell in row]) for row in self.matrix])

    def __repr__(self):
        return self.name + "\n" + str(self)


# Let's define a sample card and test the rotation function
sample_card = Card([
    [0, 1, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 0]
], "Sample")

print(sample_card)
sample_card.rotate(90)
print("\nAfter 90° rotation:\n")
print(sample_card)
