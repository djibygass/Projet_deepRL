from src.environments.bandido_v2 import card
from src.environments.bandido_v2.exceptions import invalid_card_exception
from src.environments.bandido_v2.settings.card_parser import cardParser


class line_card_parser(cardParser):

    def __init__(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.lines = file.readlines()
            self.current_line = 0
        except FileNotFoundError:
            print(f"The file at :{file_path} does not exist.")
            raise

    def has_next_line(self):
        return self.current_line < len(self.lines)

    def get_copies_of_card(self):
        if self.has_next_line():
            copies = int(self.lines[self.current_line].strip())
            self.current_line += 1
            return copies
        return 0

    def get_card(self):
        if self.has_next_line():
            card_str = self.lines[self.current_line].strip()
            self.current_line += 1
            try:
                return card(card_str)
            except invalid_card_exception as e:
                print(e)
                exit(-1)
        return None
