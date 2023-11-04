import sys


class empty_deck_exception(Exception):

    def __init__(self):
        self.message = "The deck is empty! No more cards can be drawn"
        super().__init__(self.message)
        print(self.message, file=sys.stderr)
