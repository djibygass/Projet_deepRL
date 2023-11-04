import sys


class invalid_card_exception(Exception):
    def __init__(self, message="Fatal error! The passed Card representational string was invalid!"):
        self.message = message
        super().__init__(self.message)
        print(f"Error: {self.message}", file=sys.stderr)

    def get_message(self):
        return self.message
