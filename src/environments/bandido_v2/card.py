from src.environments.bandido_v2.exceptions import invalid_card_exception


class Card:
    ROWS = 4
    COLUMNS = 3

    class InvalidCardException(Exception):
        def __init__(self):
            super().__init__("Fatal error! The passed Card representational string was invalid!")

    class Card:
        ROWS = 4
        COLUMNS = 3

        def __init__(self, representation):
            if len(representation) != self.ROWS * self.COLUMNS:
                raise InvalidCardException()

            self.matrix = [[None] * self.COLUMNS for _ in range(self.ROWS)]

            counter = 0
            for i in range(self.ROWS):
                for j in range(self.COLUMNS):
                    self.matrix[i][j] = representation[i + j + counter]
                counter += self.COLUMNS - 1

        @staticmethod
        def get_card_max_width():
            return max(Card.COLUMNS, Card.ROWS)

        def get_card_representation(self):
            return self.matrix

        # TODO: Implement rotate methods
        def rotate_clockwise_90(self):
            pass

        def rotate_counter_clockwise_90(self):
            pass
