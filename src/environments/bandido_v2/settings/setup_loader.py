from pathlib import Path
from src.environments.bandido_v2 import card, starter_card
from src.environments.bandido_v2.settings.card_parser import cardParser


class setup_loader:
    resources_path = Path("..", "resources")
    card_list_path = resources_path / "cards" / "BandidoCardsList"

    class Difficulty:
        EASY = "EASY"
        DIFFICULT = "DIFFICULT"

    def __init__(self, players, difficulty):
        self.players = players
        self.difficulty = difficulty
        self.card_set = set()

    def load_and_get_cards(self):
        parser = cardParser.get_card_parser(self.card_list_path)
        while not parser.has_next_line():
            for _ in range(parser.get_copies_of_card()):
                self.card_set.add(parser.get_card())

        return set(self.card_set)

    def get_number_of_players(self):
        return self.players

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def get_starter_card(self):
        return starter_card.get_starter_card(self.difficulty)
